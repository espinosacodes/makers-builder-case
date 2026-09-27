"""Business numbers for the "rain clause of the fiado" (Clausula de lluvia del fiado).

The mechanism: when IDEAM station 0026055120 (Universidad del Valle, Cali) records 5 mm or more of
rain between 7 a.m. and 7 p.m., the part of a cart vendor's daily fiado that he could not pay that
day is repaid in thirds over his next 3 selling days, with no surcharge, and he gets his fiado the
next morning as usual. Whoever gives the fiado (the retailer, or the wholesaler above it) carries
that float and pays the SAS a monthly fee per enrolled vendor. The SAS sells the trigger, the
written rule and the ledger. It never lends, never insures, and the vendor's money never passes
through it. See report/brief-final.md, sections 2 and 9.

This script answers the six questions of the case (initial investment, monthly fixed cost,
contribution per user, users and revenue at months 3, 6 and 12, break-even, cash to survive) for a
base case, a conservative case and the lean plan (no salary until the operation covers its costs,
persona natural for the first 6 months), and prints the views of the payer and of the vendor.

Every input is a named constant. The comment next to it gives the source, or says [ASSUMPTION]
when there is no data behind it. Run with: python3 models/business_model.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import usury_cap  # noqa: E402  (reused for the legal-loan comparison in the vendor view)

# ---------------------------------------------------------------------------------------------
# Facts with a source
# ---------------------------------------------------------------------------------------------
MINIMUM_WAGE_2026 = 1_750_905          # 2026 minimum monthly wage (research front 07, confirmed)
SELLING_DAYS_PER_MONTH = 26            # Monday to Saturday convention used across the report
VENDOR_INCOME_PER_SELLING_DAY = 38_600  # about 1.0 million a month of mixed income / 26 days
                                        # (DANE, EMICRON street vendors 2025, table 24; fact F11)
TRIGGER_DAYS_PER_YEAR = 26             # own count on IDEAM station 0026055120: 26 of 294 selling
                                       # days with 5 mm or more, 7:00 to 18:59, 27 Sep 2025 to
                                       # 26 Sep 2026 (docs/research/12-mecanismos-dia-malo.md, s.1)
FIADO_UPPER_BOUND = 62_000             # street-vendor daily sales (about 95,000) minus mixed income
                                       # (about 33,000), DANE via fronts 01 and 08 (fact P9).
                                       # Upper bound; not measured for carts in Cali
FIADO_LOW = 30_000                     # [ASSUMPTION] low case for the daily fiado
GOTA_A_GOTA_FLAT = 0.20                # flat charge per cycle (case statement; Martinez and
                                       # Rivera-Acevedo 2019 find 20.4% monthly in Cali, fact F12)
ONE_DAY_BRIDGE_FLAT = 0.10             # "diario anticipado", 10% for one day (Perez Cruz 2025,
                                       # Corabastos, Bogota; fact F24)
MICROCREDIT_ARREARS = 0.069            # formal microcredit arrears, Jul 2026 (El Tiempo with SFC
                                       # data; R58). Only a reference for the payer's loss rates
STREET_VENDORS_CALI = 17_745           # street-vendor micro-businesses in Cali A.M. (DANE, EMICRON
                                       # 24 cities 2025, table D.1_24C; CV 8.4%; fact N1)

# ---------------------------------------------------------------------------------------------
# Initial investment, before the first user (all [ASSUMPTION], no quotes yet)
# ---------------------------------------------------------------------------------------------
INITIAL_INVESTMENT = {
    "SAS registration (Ley 1258 de 2008); cost not found in sources": 600_000,
    "lawyer opinion on 5 questions (insurance reading, Ley 2300, data)": 3_000_000,
    "printed vendor cards and pilot material": 300_000,
    "rain trigger program and WhatsApp bot (own work, no cash)": 0,
    "capital to lend (none: the SAS never lends)": 0,
}

# ---------------------------------------------------------------------------------------------
# Monthly fixed cost, with or without users (all [ASSUMPTION] except the wage)
# ---------------------------------------------------------------------------------------------
FIXED_MONTHLY = {
    "founder salary, 1 minimum wage 2026": MINIMUM_WAGE_2026,
    "transport and field work": 200_000,
    "phone and mobile data": 80_000,
    "WhatsApp Business number, server, tools": 150_000,
    "accountant (SAS books, e-invoicing)": 350_000,
}
TEAM_FIXED_MONTHLY = 10_000_000        # [ASSUMPTION] small team convention used in earlier models


class Scenario:
    """One set of commercial and growth assumptions."""

    def __init__(self, name, fee, collection, direct_cost, retailers, vendors_per_retailer,
                 include_wage=True, free_first_month=True, fixed_schedule=None,
                 one_off_by_month=None, initial_investment=None, salary_from_margin=False):
        self.name = name
        self.fee = fee                          # pesos per enrolled vendor per month, paid by the payer
        self.collection = collection            # share of billed fees actually collected
        self.direct_cost = direct_cost          # pesos per vendor per month (messages, card)
        self.retailers = retailers              # function: month -> retailers signed
        self.vendors_per_retailer = vendors_per_retailer  # function: month -> vendors each
        self.include_wage = include_wage
        self.free_first_month = free_first_month  # each retailer pays from its second month
        self.fixed_schedule = fixed_schedule    # optional function: month -> fixed cost that month
        self.one_off_by_month = one_off_by_month or {}  # month -> one-off cash cost that month
        self.initial_investment = INITIAL_INVESTMENT if initial_investment is None else initial_investment
        # If True, the founder takes no salary until the month's contribution covers the fixed cost,
        # and after that takes at most one minimum wage, only out of the month's surplus.
        self.salary_from_margin = salary_from_margin

    def fixed_monthly(self):
        """Steady-state fixed cost, the one the break-even vendor count is measured against."""
        total = sum(FIXED_MONTHLY.values())
        return total if self.include_wage else total - MINIMUM_WAGE_2026

    def fixed_in_month(self, month):
        if self.fixed_schedule is None:
            return self.fixed_monthly()
        return self.fixed_schedule(month)

    def contribution_per_vendor(self):
        # Expected non-payment lives here: uncollected fees. No money of the vendor moves through
        # the SAS, so there is no credit loss for the SAS; the loss on deferred fiado stays with
        # the payer and is shown in payer_view().
        return self.fee * self.collection - self.direct_cost

    def vendors(self, month):
        if month < 1:
            return 0
        return self.retailers(month) * self.vendors_per_retailer(month)

    def paying_vendors(self, month):
        if not self.free_first_month:
            return self.vendors(month)
        return min(self.vendors(month - 1), self.vendors(month))


def base_retailers(month):
    # [ASSUMPTION] one person signs retailers through the vendors of the Universidades MIO station,
    # then through retailers that buy from the same wholesaler: 4 new retailers a month from month 7
    ramp = {1: 2, 2: 3, 3: 4, 4: 6, 5: 9, 6: 12, 7: 16, 8: 20, 9: 24, 10: 28, 11: 32, 12: 36}
    return ramp.get(month, 36 + 4 * (month - 12))


def base_vendors_per_retailer(month):
    # [ASSUMPTION] no data on how many carts one retailer supplies (first field question)
    ramp = {1: 8, 2: 9, 3: 10, 4: 11, 5: 12, 6: 12}
    return ramp.get(month, 13)


def conservative_retailers(month):
    # [ASSUMPTION] half the signing pace: one new retailer a month up to month 6, then 2 a month
    return month if month <= 6 else 6 + 2 * (month - 6)


def conservative_vendors_per_retailer(month):
    # [ASSUMPTION] smaller retailers: 5 vendors in month 1, 8 from month 4
    return {1: 5, 2: 6, 3: 7}.get(month, 8)


BASE = Scenario(
    name="base",
    fee=4_000,              # [ASSUMPTION] no price precedent; range tested 2,000 to 6,000
    collection=0.90,        # [ASSUMPTION] 10% of billed fees never collected
    direct_cost=800,        # [ASSUMPTION] WhatsApp messages and printed card per vendor per month
    retailers=base_retailers,
    vendors_per_retailer=base_vendors_per_retailer,
)

CONSERVATIVE = Scenario(
    name="conservative",
    fee=4_000,              # same price, so the gap with the base comes from volume and collection
    collection=0.80,        # [ASSUMPTION] 20% of billed fees never collected
    direct_cost=1_000,      # [ASSUMPTION] messages 25% more expensive than in the base
    retailers=conservative_retailers,
    vendors_per_retailer=conservative_vendors_per_retailer,
)

# ---------------------------------------------------------------------------------------------
# Lean plan (founder decision, 27 Sep 2026): same base ramp and prices, but
#   - no founder salary until the operation covers its own costs; after that the salary comes
#     only out of the monthly surplus, capped at one minimum wage;
#   - first months as persona natural: no SAS registration and no accountant until month 7;
#   - the lawyer's opinion either free (university consultorio juridico) or paid.
# ---------------------------------------------------------------------------------------------
LEAN_PERSONA_NATURAL_MONTHS = 6        # months 1 to 6 without SAS and without accountant
LEAN_SAS_MONTH = LEAN_PERSONA_NATURAL_MONTHS + 1  # SAS registered and accountant hired in month 7
SAS_REGISTRATION = 600_000             # [ASSUMPTION] same figure as in INITIAL_INVESTMENT
LEGAL_OPINION_PAID = 3_000_000         # [ASSUMPTION] same figure as in INITIAL_INVESTMENT
LEGAL_OPINION_FREE = 0                 # [ASSUMPTION, not verified] university consultorio juridico
PRINTED_MATERIAL = 300_000             # [ASSUMPTION] vendor cards and pilot material
ACCOUNTANT_MONTHLY = FIXED_MONTHLY["accountant (SAS books, e-invoicing)"]


def lean_fixed(month):
    """Fixed cost without founder salary; the accountant only starts with the SAS."""
    without_wage = sum(FIXED_MONTHLY.values()) - MINIMUM_WAGE_2026
    if month < LEAN_SAS_MONTH:
        return without_wage - ACCOUNTANT_MONTHLY
    return without_wage


def lean_scenario(legal_opinion, label):
    return Scenario(
        name=f"lean, legal opinion {label}",
        fee=BASE.fee, collection=BASE.collection, direct_cost=BASE.direct_cost,
        retailers=base_retailers, vendors_per_retailer=base_vendors_per_retailer,
        include_wage=False, fixed_schedule=lean_fixed,
        one_off_by_month={LEAN_SAS_MONTH: SAS_REGISTRATION},
        initial_investment={
            "printed vendor cards and pilot material": PRINTED_MATERIAL,
            "lawyer opinion on 5 questions": legal_opinion,
        },
        salary_from_margin=True,
    )


LEAN_FREE_LEGAL = lean_scenario(LEGAL_OPINION_FREE, "free")
LEAN_PAID_LEGAL = lean_scenario(LEGAL_OPINION_PAID, "paid")


def lean_conservative(legal_opinion, label):
    """Lean cost structure on the conservative ramp (half the signing pace, 80% collection)."""
    return Scenario(
        name=f"lean conservative, legal opinion {label}",
        fee=CONSERVATIVE.fee, collection=CONSERVATIVE.collection,
        direct_cost=CONSERVATIVE.direct_cost,
        retailers=conservative_retailers, vendors_per_retailer=conservative_vendors_per_retailer,
        include_wage=False, fixed_schedule=lean_fixed,
        one_off_by_month={LEAN_SAS_MONTH: SAS_REGISTRATION},
        initial_investment={
            "printed vendor cards and pilot material": PRINTED_MATERIAL,
            "lawyer opinion on 5 questions": legal_opinion,
        },
        salary_from_margin=True,
    )


LEAN_CONSERVATIVE_FREE_LEGAL = lean_conservative(LEGAL_OPINION_FREE, "free")
LEAN_CONSERVATIVE_PAID_LEGAL = lean_conservative(LEGAL_OPINION_PAID, "paid")

HORIZON_MONTHS = 60
MILESTONE_MONTHS = (3, 6, 12)


def simulate(scenario, horizon=HORIZON_MONTHS):
    """Month by month result. Break-even is the first month whose contribution covers fixed cost."""
    fixed = scenario.fixed_monthly()
    unit = scenario.contribution_per_vendor()
    cumulative = -sum(scenario.initial_investment.values())
    trough, trough_month = -cumulative, 0
    rows, break_even_month = [], None
    for m in range(1, horizon + 1):
        paying = scenario.paying_vendors(m)
        billed = paying * scenario.fee
        contribution = paying * unit
        operating = contribution - scenario.fixed_in_month(m)
        if break_even_month is None and operating >= 0:
            break_even_month = m
        salary = 0
        if scenario.salary_from_margin and break_even_month is not None:
            salary = max(0, min(MINIMUM_WAGE_2026, operating))
        result = operating - salary - scenario.one_off_by_month.get(m, 0)
        cumulative += result
        if -cumulative > trough:
            trough, trough_month = -cumulative, m
        rows.append({
            "month": m, "retailers": scenario.retailers(m), "vendors": scenario.vendors(m),
            "paying": paying, "billed": billed, "collected": billed * scenario.collection,
            "contribution": contribution, "salary": salary, "result": result,
            "cumulative": cumulative,
        })
    return {
        "rows": rows, "fixed": fixed, "unit": unit,
        "break_even_vendors": fixed / unit if unit > 0 else float("inf"),
        "break_even_month": break_even_month,
        "cash_needed": trough, "trough_month": trough_month,
    }


def verdict(scenario, sim):
    """Plain statement of whether and why the model closes."""
    m = sim["break_even_month"]
    if sim["unit"] <= 0:
        return "DOES NOT CLOSE: each vendor costs more than he brings, no volume fixes it."
    if m is None:
        return (f"DOES NOT CLOSE within {HORIZON_MONTHS} months: at this signing pace the paying "
                f"vendors never reach {sim['break_even_vendors']:,.0f}.")
    if m > 12:
        month12 = sim["rows"][11]
        return (f"Does not close in the first 12 months (month 12 result {month12['result']:,.0f}); "
                f"it closes in month {m}. The reason is volume at a {scenario.fee:,} fee that nobody has paid "
                f"yet, not credit risk, because the SAS does not lend.")
    return f"Closes in month {m}."


def payer_view(fiado, deferred_default, fee=4_000, carrier_rate=0.20, gross_margin=0.10,
               float_days=2.5, gap_share=1.0):
    """Yearly cost and benefit of the clause for whoever carries the float, per vendor.

    carrier_rate: [ASSUMPTION] cost of money of the retailer, 20% effective annual.
    gross_margin: [ASSUMPTION] retailer gross margin on the fiado goods, 10%, no source.
    float_days: [ASSUMPTION] average days until the deferred fiado comes back (thirds plus Sundays).
    gap_share: [ASSUMPTION] share of the fiado left unpaid on a trigger day (50% to 100%).
    """
    deferred = TRIGGER_DAYS_PER_YEAR * fiado * gap_share
    float_cost = deferred * ((1 + carrier_rate) ** (float_days / 365) - 1)
    loss = deferred * deferred_default
    fees = fee * 12
    margin_per_vendor = fiado * SELLING_DAYS_PER_MONTH * 12 * gross_margin
    churn_to_pay_off = (float_cost + loss + fees) / margin_per_vendor
    return {"deferred": deferred, "float_cost": float_cost, "loss": loss, "fees": fees,
            "margin": margin_per_vendor, "churn_to_pay_off": churn_to_pay_off}


def vendor_view(fiado):
    """What covering one rain day's fiado costs the vendor on each path."""
    legal_flat = usury_cap.max_flat_charge(usury_cap.USURY_CAPS[0][0], 30)  # 30 daily installments
    paths = {
        "gota a gota, 20% flat": fiado * GOTA_A_GOTA_FLAT,
        "one-day informal bridge, 10%": fiado * ONE_DAY_BRIDGE_FLAT,
        f"legal daily loan at the usury cap ({legal_flat:.2%} flat, 30 installments; "
        f"not offered at this size)": fiado * legal_flat,
        "rain clause": 0,
    }
    return {k: (v, v / VENDOR_INCOME_PER_SELLING_DAY) for k, v in paths.items()}


def perishable_load(fiado, gap_share):
    """If the unsold goods spoil, the clause only spreads the loss: extra payment per day."""
    per_day = fiado * gap_share / 3
    return per_day, per_day / VENDOR_INCOME_PER_SELLING_DAY


def print_scenario(scenario):
    sim = simulate(scenario)
    print(f"\n=== {scenario.name.upper()} CASE ===")
    print(f"Fee {scenario.fee:,} x collection {scenario.collection:.0%} - direct cost "
          f"{scenario.direct_cost:,} = contribution per vendor per month {sim['unit']:,.0f}")
    print(f"Monthly fixed cost: {sim['fixed']:,.0f}")
    for m in MILESTONE_MONTHS:
        r = sim["rows"][m - 1]
        print(f"  month {m:>2}: retailers {r['retailers']:>3}, vendors {r['vendors']:>4}, paying "
              f"{r['paying']:>4}, billed {r['billed']:>10,.0f}, collected {r['collected']:>10,.0f}, "
              f"contribution {r['contribution']:>10,.0f}, result {r['result']:>11,.0f}")
    print(f"Break-even vendors (paying): {sim['break_even_vendors']:,.0f} "
          f"({sim['break_even_vendors'] / STREET_VENDORS_CALI:.1%} of Cali A.M. street vendors)")
    m = sim["break_even_month"]
    if m:
        r = sim["rows"][m - 1]
        print(f"Break-even month: {m} ({r['retailers']} retailers, {r['vendors']} vendors, "
              f"{r['paying']} paying)")
    else:
        print(f"Break-even month: not reached within {HORIZON_MONTHS} months")
        for mm in (24, 36):
            r = sim["rows"][mm - 1]
            print(f"  month {mm}: paying {r['paying']}, result {r['result']:,.0f}, "
                  f"cumulative {r['cumulative']:,.0f}")
    print(f"Cash needed (initial investment plus losses to the deepest point): "
          f"{sim['cash_needed']:,.0f} (deepest point in month {sim['trough_month']})")
    print(f"Verdict: {verdict(scenario, sim)}")
    return sim


if __name__ == "__main__":
    print("Initial investment")
    for item, value in INITIAL_INVESTMENT.items():
        print(f"  {item:70s} {value:>11,.0f}")
    print(f"  {'TOTAL':70s} {sum(INITIAL_INVESTMENT.values()):>11,.0f}")
    print("Monthly fixed cost")
    for item, value in FIXED_MONTHLY.items():
        print(f"  {item:70s} {value:>11,.0f}")
    print(f"  {'TOTAL':70s} {sum(FIXED_MONTHLY.values()):>11,.0f}")

    results = {}
    for sc in (BASE, CONSERVATIVE):
        results[sc.name] = print_scenario(sc)
        no_wage = Scenario(sc.name + " without founder salary", sc.fee, sc.collection,
                           sc.direct_cost, sc.retailers, sc.vendors_per_retailer, include_wage=False)
        print_scenario(no_wage)

    print("\n=== LEAN PLAN (no salary until the operation covers its costs; base and conservative ramps) ===")
    for sc in (LEAN_FREE_LEGAL, LEAN_PAID_LEGAL,
               LEAN_CONSERVATIVE_FREE_LEGAL, LEAN_CONSERVATIVE_PAID_LEGAL):
        sim = print_scenario(sc)
        print(f"  initial investment {sum(sc.initial_investment.values()):,.0f}; fixed cost months 1 to "
              f"{LEAN_PERSONA_NATURAL_MONTHS} {lean_fixed(1):,.0f}, from month {LEAN_SAS_MONTH} "
              f"{lean_fixed(LEAN_SAS_MONTH):,.0f} plus SAS registration {SAS_REGISTRATION:,.0f} once")
        full_wage = next((r["month"] for r in sim["rows"] if r["salary"] >= MINIMUM_WAGE_2026), None)
        print(f"  first month the surplus pays a full minimum wage: {full_wage}")
    base_sim = results["base"]
    print(f"Comparison, base with salary from month 1: cash needed {base_sim['cash_needed']:,.0f}, "
          f"break-even month {base_sim['break_even_month']}")

    print("\nSensitivity on the base ramp: fee x founder salary")
    for fee in (2_000, 4_000, 6_000):
        for wage in (True, False):
            sc = Scenario("s", fee, BASE.collection, BASE.direct_cost, base_retailers,
                          base_vendors_per_retailer, include_wage=wage)
            sim = simulate(sc, horizon=36)
            month = sim["break_even_month"] or "not in 36 months"
            print(f"  fee {fee:>5,} {'with' if wage else 'without':7s} salary: break-even "
                  f"{sim['break_even_vendors']:>6,.0f} vendors, month {month}, cash needed "
                  f"{sim['cash_needed']:>12,.0f}")
    print(f"Team of {TEAM_FIXED_MONTHLY:,} a month: {TEAM_FIXED_MONTHLY / BASE.contribution_per_vendor():,.0f} "
          f"paying vendors to break even")

    print("\nFunding of the lean cash (founder decision, 27 Sep 2026): own capital, personal or family "
          "savings [ASSUMPTION], never loans taken from the public (captacion line, Decreto 1981 de "
          "1988). Fondo Emprender only as a conditional upside (no open call for Cali today); "
          "Fundacion WWB Colombia as a pilot ally, not as money; BID Lab only for a later regional "
          "phase after 12 months of pilot data. The fellowship is not counted.")

    print("\nPayer view (retailer or wholesaler), per vendor per year, all the fiado deferred")
    for fiado in (FIADO_LOW, FIADO_UPPER_BOUND):
        for d in (0.01, 0.03, 0.10):
            v = payer_view(fiado, d)
            print(f"  fiado {fiado:>6,} default {d:>4.0%}: deferred {v['deferred']:>9,.0f}, float "
                  f"{v['float_cost']:>6,.0f}, loss {v['loss']:>7,.0f}, fee {v['fees']:>6,.0f} | "
                  f"margin per vendor {v['margin']:>10,.0f} | pays off if it avoids losing "
                  f"{v['churn_to_pay_off']:.1%} of vendors a year")
    print(f"  reference: formal microcredit arrears {MICROCREDIT_ARREARS:.1%} (R58)")

    print(f"\nVendor view: covering one rain day's fiado (income {VENDOR_INCOME_PER_SELLING_DAY:,} "
          f"per selling day)")
    for fiado in (FIADO_LOW, FIADO_UPPER_BOUND):
        for path, (cost, share) in vendor_view(fiado).items():
            print(f"  fiado {fiado:>6,} {path:80s} {cost:>7,.0f} ({share:.0%} of a day's income)")

    print("\nIf the goods spoil (the clause does not cover this): extra payment on each of 3 days")
    for gap in (0.5, 1.0):
        per_day, share = perishable_load(FIADO_UPPER_BOUND, gap)
        print(f"  fiado {FIADO_UPPER_BOUND:,}, {gap:.0%} unpaid: {per_day:,.0f} a day "
              f"({share:.0%} of a day's income)")
