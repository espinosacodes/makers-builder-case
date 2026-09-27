"""Viability model for the "fiado bridge" (mechanism E1, refined): a rain-triggered deferral of the
vendor's daily fiado, carried by the supply chain that already gives the fiado (retailer, and the
wholesaler above it when one accepts), with our SAS selling the rule, the public trigger and the
ledger to whoever carries the float. Nobody lends money to the vendor and no money passes through us.
See docs/research/12-mecanismos-dia-malo.md for the mechanism and models/bad_day_mechanisms.py
for the chain-side cost with a 10 million fixed-cost convention; this file uses a lean pilot cost base.

Every number is an assumption unless a source is named in the comment next to it.
Sources used:
- Trigger days: own count on IDEAM station 0026055120 (Universidad del Valle, Cali), 5 mm or more
  between 7:00 and 18:59, Monday to Saturday, 27 Sep 2025 to 26 Sep 2026 (models/bad_day_mechanisms.py).
- Fiado upper bound 62,000: street-vendor daily sales (about 95,000) minus mixed income (about 33,000),
  DANE EMICRON street vendors 2025, via research fronts 01 and 08. Not measured for carts.
- Minimum wage 2026: 1,750,905 (research front 07, confirmed via Holland & Knight).
- Informal one-day bridge: "diario anticipado" at 10% for the day (Perez Cruz 2025, Bogota).
- Gota a gota: 20% flat per cycle (case statement; Martinez and Rivera-Acevedo 2019 find 20.4% monthly in Cali).
"""

SELLING_DAYS_PER_MONTH = 26
TRIGGER_DAYS_PER_YEAR = 26          # IDEAM own count, Monday to Saturday
EARNED_DAYS_PER_YEAR = 0            # base: rain only; variant: 6 (1 earned non-rain day a month, used half the time)
FLOAT_DAYS = 2.5                    # assumption: deferred fiado repaid in thirds over the next 3 selling days

# Our fixed monthly cost, with or without users (all assumptions except the wage).
FIXED_MONTHLY = {
    "founder, 1 minimum wage": 1_750_905,
    "transport and field work": 200_000,
    "phone and mobile data": 80_000,
    "WhatsApp Business number, server, tools": 150_000,
    "accountant (SAS books, e-invoicing)": 350_000,
}

# Up-front investment before the first user (assumptions; quotes pending).
INITIAL = {
    "SAS registration (cost not found in sources)": 600_000,
    "financial lawyer opinion on 5 questions": 3_000_000,
    "printed cards and pilot material": 300_000,
    "bot and IDEAM trigger (own work, no cash)": 0,
}

FEE_PER_VENDOR_MONTH = 4_000        # paid by the wholesaler or retailer; tested in the pilot (range 2,000 to 6,000)
FEE_COLLECTION = 0.90               # assumption: 10% of billed fees never collected (payer churn or non-payment)
DIRECT_COST_PER_VENDOR_MONTH = 800  # assumption: WhatsApp messages and printed card, per vendor

# Vendors covered at the end of each month (assumption: retailers x vendors per retailer).
RETAILERS = {1: 2, 2: 3, 3: 4, 4: 6, 5: 9, 6: 12, 7: 16, 8: 20, 9: 24, 10: 28, 11: 32, 12: 36}
VENDORS_PER_RETAILER = {1: 8, 2: 9, 3: 10, 4: 11, 5: 12, 6: 12}   # 13 from month 7
FREE_FIRST_MONTH = True             # each retailer pays from its second month


def vendors_in_month(m):
    retailers = RETAILERS.get(m, 36 + 4 * (m - 12))
    per = VENDORS_PER_RETAILER.get(m, 13)
    return retailers, retailers * per


def paying_vendors(m):
    if not FREE_FIRST_MONTH:
        return vendors_in_month(m)[1]
    prev = vendors_in_month(m - 1)[1] if m > 1 else 0
    return min(prev, vendors_in_month(m)[1])


def contribution_per_vendor(fee=FEE_PER_VENDOR_MONTH):
    return fee * FEE_COLLECTION - DIRECT_COST_PER_VENDOR_MONTH


def simulate(fee=FEE_PER_VENDOR_MONTH, fixed=None, months=36):
    """Monthly result, break-even month and deepest cumulative cash point."""
    fixed = sum(FIXED_MONTHLY.values()) if fixed is None else fixed
    unit = contribution_per_vendor(fee)
    cumulative = trough = -sum(INITIAL.values())
    break_even_month = None
    for m in range(1, months + 1):
        cumulative += paying_vendors(m) * unit - fixed
        trough = min(trough, cumulative)
        if break_even_month is None and paying_vendors(m) * unit >= fixed:
            break_even_month = m
    return break_even_month, -trough


def retailer_view(fiado, repay_default, fee=FEE_PER_VENDOR_MONTH, own_rate=0.20, margin=0.10,
                  earned_days=EARNED_DAYS_PER_YEAR):
    """Yearly cost and benefit of the pact for whoever carries the float, per vendor."""
    deferred = (TRIGGER_DAYS_PER_YEAR + earned_days) * fiado
    float_cost = deferred * ((1 + own_rate) ** (FLOAT_DAYS / 365) - 1)
    loss = deferred * repay_default
    fees = fee * 12
    yearly_margin = fiado * SELLING_DAYS_PER_MONTH * 12 * margin
    churn_to_break_even = (float_cost + loss + fees) / yearly_margin
    return deferred, float_cost, loss, fees, yearly_margin, churn_to_break_even


def vendor_view(fiado):
    """What the same days cost the vendor today if each one is bridged informally."""
    days = TRIGGER_DAYS_PER_YEAR
    one_day_bridge = fiado * 0.10          # Corabastos "diario anticipado"
    gota_cycle = fiado * 0.20              # a gota a gota cycle for the same amount
    return days, one_day_bridge, gota_cycle


if __name__ == "__main__":
    fixed = sum(FIXED_MONTHLY.values())
    initial = sum(INITIAL.values())
    unit = contribution_per_vendor()
    print(f"Initial investment: {initial:,.0f}")
    print(f"Fixed monthly cost: {fixed:,.0f}")
    print(f"Contribution per vendor per month: {unit:,.0f}")
    print(f"Break-even vendors: {fixed / unit:,.0f}")
    cumulative = -initial
    trough = cumulative
    break_even_month = None
    for m in range(1, 37):
        retailers, active = vendors_in_month(m)
        paying = paying_vendors(m)
        result = paying * unit - fixed
        cumulative += result
        trough = min(trough, cumulative)
        if result >= 0 and break_even_month is None:
            break_even_month = m
        if m in (3, 6, 12, 18, 24) or m == break_even_month:
            print(f"month {m:>2}: retailers {retailers:>3} vendors {active:>4} paying {paying:>4} "
                  f"monthly result {result:>11,.0f} cumulative {cumulative:>12,.0f}")
    print(f"Break-even month: {break_even_month}; cash needed (deepest cumulative point): {-trough:,.0f}")

    print("Sensitivity: break-even vendors by fee and fixed cost")
    for fee in (2_000, 4_000, 6_000):
        for label, cost in (("with founder wage", fixed), ("without founder wage", fixed - 1_750_905)):
            print(f"  fee {fee:>5,} {label:21s}: {cost / contribution_per_vendor(fee):>6,.0f} vendors")

    print("Scenarios: break-even month and cash needed")
    for fee in (2_000, 4_000, 6_000):
        for label, cost in (("with founder wage", fixed), ("without founder wage", fixed - 1_750_905)):
            month, cash = simulate(fee, cost)
            print(f"  fee {fee:>5,} {label:21s}: break-even month {month}, cash needed {cash:,.0f}")

    print("Retailer view, per vendor per year")
    for fiado in (30_000, 62_000):
        for d in (0.01, 0.03, 0.10):
            deferred, fc, loss, fees, ym, churn = retailer_view(fiado, d)
            print(f"  fiado {fiado:>6,} default {d:>4.0%}: deferred {deferred:>9,.0f} float {fc:>6,.0f} "
                  f"loss {loss:>7,.0f} fee {fees:>6,.0f} | margin kept {ym:>10,.0f} "
                  f"| breaks even if it saves {churn:.1%} of vendors a year")

    print("Variant with 1 earned non-rain day a month (used half the time)")
    for d in (0.03, 0.10):
        *_, churn = retailer_view(62_000, d, earned_days=6)
        print(f"  fiado 62,000 default {d:.0%}: breaks even if it saves {churn:.1%} of vendors a year")

    print("Vendor view")
    for fiado in (30_000, 62_000):
        days, bridge, gota = vendor_view(fiado)
        print(f"  fiado {fiado:>6,}: {days} rain days a year; informal one-day bridge {bridge:,.0f} per day; "
              f"gota a gota cycle {gota:,.0f} per day")
