"""Maximum legal flat charge for a daily-installment loan under the Colombian usury cap.

Installments run Monday to Saturday, the first one the day after disbursement.
The effective annual rate is computed from the real daily cash flows.
Caps are the SFC certification for 1 to 30 September 2026 (Resolucion 1260 de 2026).
They change every month, so update USURY_CAPS before reusing the numbers.
"""
import datetime as dt

USURY_CAPS = [
    (0.8813, "popular productivo urbano, sep 2026"),
    (0.6687, "consumo de bajo monto"),
    (0.2924, "consumo y ordinario"),
]
INSTALLMENT_COUNTS = [24, 30, 36, 48]
INFORMAL_FLAT_CHARGE = 0.20


def schedule(n, start=dt.date(2026, 10, 5)):
    """Day offsets of n Monday-to-Saturday installments after a disbursement on `start`."""
    days, d = [], start
    while len(days) < n:
        d += dt.timedelta(days=1)
        if d.weekday() != 6:
            days.append((d - start).days)
    return days


def effective_annual_rate(flat, n):
    """Effective annual rate of a loan of 1 repaid as n equal installments of (1 + flat) / n."""
    days = schedule(n)
    installment = (1 + flat) / n
    lo, hi = 0.0, 0.2
    for _ in range(200):
        daily = (lo + hi) / 2
        present_value = sum(installment / (1 + daily) ** t for t in days)
        if present_value > 1:
            lo = daily
        else:
            hi = daily
    return (1 + daily) ** 365 - 1, days[-1]


def max_flat_charge(cap, n):
    """Largest flat charge whose effective annual rate stays under `cap`."""
    lo, hi = 0.0, 1.0
    for _ in range(200):
        flat = (lo + hi) / 2
        rate, _ = effective_annual_rate(flat, n)
        if rate > cap:
            hi = flat
        else:
            lo = flat
    return flat


if __name__ == "__main__":
    for cap, name in USURY_CAPS:
        print(name)
        for n in INSTALLMENT_COUNTS:
            flat = max_flat_charge(cap, n)
            _, last_day = effective_annual_rate(flat, n)
            legal = 100_000 * (1 + flat) / n
            informal = 100_000 * (1 + INFORMAL_FLAT_CHARGE) / n
            print(f"  {n} installments ({last_day} days): max flat charge {flat * 100:.2f}% | "
                  f"per 100,000: {legal:,.0f}/day legal vs {informal:,.0f}/day informal at 20%")
    for n in (24, 36):
        rate, last_day = effective_annual_rate(INFORMAL_FLAT_CHARGE, n)
        print(f"informal 20% flat over {n} installments: effective annual rate {rate * 100:,.0f}% ({last_day} days)")
