"""Rough yearly unit economics of mechanism A (daily-installment credit line through the shopkeeper).

Assumptions (see docs/research/00-sintesis.md, section 6.0; none of the loss rates is measured in Colombia):
- 8 cycles a year, each of 36 Monday-to-Saturday installments (6 weeks).
- Flat charge of 3.5% per cycle, under the 3.71% legal maximum of September 2026 (see usury_cap.py).
- Shopkeeper keeps 20% of the charge; funding at 12% effective annual on an average balance
  of 52% of the ticket for about 1.4 months; 1,000 pesos of operating cost per cycle.
"""

FIXED_MONTHLY_COST = 10_000_000

TICKET_PATHS = {
    "path to 1 million": [200_000, 400_000, 700_000] + [1_000_000] * 5,
    "street vendor path (half of weekly income)": [100_000, 150_000, 200_000] + [250_000] * 5,
}


def yearly_net(tickets, fee=0.035, first_loss=0.06, renewal_loss=0.015,
               shopkeeper_share=0.20, funding_rate=0.12, ops_per_cycle=1_000):
    monthly_funding = (1 + funding_rate) ** (1 / 12) - 1
    revenue = sum(t * fee for t in tickets)
    losses = sum(t * (first_loss if i == 0 else renewal_loss) for i, t in enumerate(tickets))
    funding = sum(t * 0.52 * monthly_funding * 1.4 for t in tickets)
    shopkeeper = revenue * shopkeeper_share
    net = revenue - losses - shopkeeper - funding - ops_per_cycle * len(tickets)
    return revenue, losses, shopkeeper, funding, net


if __name__ == "__main__":
    for name, tickets in TICKET_PATHS.items():
        for renewal_loss in (0.01, 0.015, 0.03):
            revenue, losses, shopkeeper, funding, net = yearly_net(tickets, renewal_loss=renewal_loss)
            active_users = FIXED_MONTHLY_COST * 12 / net if net > 0 else float("inf")
            print(f"{name:44s} renewal loss {renewal_loss * 100:.1f}%: revenue {revenue:>8,.0f} "
                  f"loss {losses:>8,.0f} shopkeeper {shopkeeper:>6,.0f} funding {funding:>6,.0f} "
                  f"net/year {net:>8,.0f} | users to cover fixed cost {active_users:>9,.0f}")
