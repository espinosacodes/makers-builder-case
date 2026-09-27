"""Rough unit economics of the two bad-day mechanisms (docs/research/12-mecanismos-dia-malo.md).

E "El puente del fiado": on a rain-trigger day the vendor's fiado payment moves to the next dry
selling days; the float is carried upstream (wholesaler in E1, our own capital lent to the
retailer in E2). Nobody lends to the vendor.
F "El dia de lluvia pagado": a daily premium bundled into the fiado buys a parametric payout
from a licensed insurer when the rain trigger fires; we are only a distribution channel.

Every input below is an assumption unless a source is named. Sources:
- Trigger days: own count on IDEAM station 0026055120 (Universidad del Valle), 5 mm or more between
  7:00 and 18:59, Monday to Saturday, 27 Sep 2025 to 26 Sep 2026: 26 of 294 days with data
  (docs/research/12b-proteccion-dia-malo.md and scratchpad rain_cali.py).
- "Bad month" layer: days beyond the 3rd trigger day of a calendar month in the same window: 8.
- Fiado of 62,000 pesos: upper bound = street-vendor daily sales (about 95,000) minus mixed income
  (about 33,000), DANE via fronts 01 and 08. Not measured for carts. 30,000 is a pure assumption.
- Mixed income per selling day: about 38,000 (33,000 x 30 / 26 selling days; synthesis 10.3 #19).
- Microinsurance loss ratio 32.3% and commercialization cost 24.3% of premiums: RIF 2025, p. 172.
- Fixed monthly cost of 10,000,000: same convention as models/unit_economics.py.
- Corabastos "diario anticipado" at 10% for the day: Perez Cruz 2025, p. 7 (Bogota, not Cali).
- Ordinary usury cap 29.24% E.A. (Sep 2026): SFC Resolucion 1260 de 2026.
"""

FIXED_MONTHLY_COST = 10_000_000
SELLING_DAYS_PER_YEAR = 300
TRIGGER_DAYS_PER_YEAR = 26
BAD_MONTH_LAYER_DAYS = 8
MIXED_INCOME_PER_DAY = 38_000
LOSS_RATIO = 0.323
CHANNEL_SHARE = 0.243
USURY_ORDINARY = 0.2924


def period_rate(annual, days):
    return (1 + annual) ** (days / 365) - 1


def mechanism_e(fiado, gap_share, default_rate, float_days=2.5, wholesaler_cost=0.20):
    """Yearly cost per vendor of deferring the unpaid part of the fiado on trigger days."""
    deferred = TRIGGER_DAYS_PER_YEAR * gap_share * fiado
    float_cost = deferred * period_rate(wholesaler_cost, float_days)
    default_cost = deferred * default_rate
    corabastos_price = deferred * 0.10  # what the informal market charges for a one-day bridge
    return deferred, float_cost, default_cost, corabastos_price


def mechanism_e2_lender(fiado, gap_share, retailer_default, float_days=2.5, funding=0.12):
    """Yearly result per vendor if we lend the float to the retailer at the ordinary usury cap."""
    deferred = TRIGGER_DAYS_PER_YEAR * gap_share * fiado
    interest = deferred * period_rate(USURY_ORDINARY, float_days)
    funding_cost = deferred * period_rate(funding, float_days)
    loss = deferred * retailer_default
    return interest, funding_cost, loss, interest - funding_cost - loss


def mechanism_f(payout, events=TRIGGER_DAYS_PER_YEAR, loss_ratio=LOSS_RATIO):
    """Premium per selling day for a parametric payout, and our channel revenue per month."""
    pure = events * payout / SELLING_DAYS_PER_YEAR
    commercial = pure / loss_ratio
    channel_month = commercial * CHANNEL_SHARE * SELLING_DAYS_PER_YEAR / 12
    return pure, commercial, commercial / MIXED_INCOME_PER_DAY, channel_month


if __name__ == "__main__":
    print("E1: wholesaler carries the float (yearly, per vendor)")
    for fiado in (30_000, 62_000):
        for gap in (0.5, 1.0):
            for dflt in (0.02, 0.05, 0.10):
                d, f, l, c = mechanism_e(fiado, gap, dflt)
                print(f"  fiado {fiado:>6,} gap {gap:.0%} default {dflt:>4.0%}: deferred {d:>9,.0f} "
                      f"float {f:>6,.0f} default {l:>7,.0f} | informal one-day price {c:>7,.0f}")
    print("E fee: vendors needed to cover the fixed monthly cost")
    for fee in (2_000, 4_000, 6_000):
        print(f"  {fee:>5,} per active vendor per month -> {FIXED_MONTHLY_COST / fee:>6,.0f} vendors")
    print("E2: we lend the float to the retailer at the ordinary usury cap (yearly, per vendor)")
    for dflt in (0.0, 0.01, 0.03):
        i, fc, l, n = mechanism_e2_lender(62_000, 1.0, dflt)
        print(f"  retailer default {dflt:.0%}: interest {i:>6,.0f} funding {fc:>6,.0f} loss {l:>7,.0f} net {n:>8,.0f}")
    print("F: parametric premium per selling day")
    cases = [("full fiado 62,000 every trigger day", 62_000, TRIGGER_DAYS_PER_YEAR),
             ("perishable loss 15,000 every trigger day", 15_000, TRIGGER_DAYS_PER_YEAR),
             ("bad-month layer 30,000 from 4th trigger day", 30_000, BAD_MONTH_LAYER_DAYS)]
    for name, payout, events in cases:
        p, c, share, ch = mechanism_f(payout, events)
        print(f"  {name:44s}: pure {p:>6,.0f} commercial {c:>6,.0f} ({share:.1%} of daily income) "
              f"| our channel revenue {ch:>6,.0f}/vendor/month -> {FIXED_MONTHLY_COST / ch:>6,.0f} vendors")
    premium = 500
    payout = premium * SELLING_DAYS_PER_YEAR * LOSS_RATIO / TRIGGER_DAYS_PER_YEAR
    print(f"F reverse: a {premium} peso daily premium buys a payout of about {payout:,.0f} per trigger day")
