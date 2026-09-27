r"""Rain-day counts for the IDEAM Universidad del Valle station (Cali), as used in Annex F.

Input: univalle_raw.csv, the 10-minute precipitation records of station 0026055120 from datos.gov.co
(dataset s54a-sgyg). Download it with:

  curl -G 'https://www.datos.gov.co/resource/s54a-sgyg.csv' \
    --data-urlencode "\$select=fechaobservacion,valorobservado,codigosensor,nombreestacion" \
    --data-urlencode "\$where=codigoestacion='0026055120' AND fechaobservacion>='2024-09-04T00:00:00'" \
    --data-urlencode '$limit=400000' -o univalle_raw.csv

Method: drop duplicated timestamps (keep the max), sum rain between 07:00 and 18:59, keep only days
with at least 60 of the 72 daytime records, trigger day = 5 mm or more, selling day = Monday to Saturday.

Usage: python3 models/rain_cali.py [path/to/univalle_raw.csv]
"""

import collections
import csv
import datetime as dt
import sys

THRESHOLD_MM = 5.0
MIN_RECORDS = 60
WINDOW = (dt.date(2025, 9, 27), dt.date(2026, 9, 26))


def load_days(path):
    records = {}
    with open(path, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            key = row["fechaobservacion"][:16]
            records[key] = max(records.get(key, 0.0), float(row["valorobservado"]))
    rain = collections.defaultdict(float)
    count = collections.Counter()
    for key, mm in records.items():
        hour = int(key[11:13])
        if 7 <= hour <= 18:
            day = dt.date.fromisoformat(key[:10])
            rain[day] += mm
            count[day] += 1
    return {d: rain[d] for d in count if count[d] >= MIN_RECORDS}


def runs(days, rain):
    """Lengths of streaks of consecutive calendar days that are all trigger days."""
    lengths, current, prev = [], 0, None
    for d in sorted(days):
        if rain[d] >= THRESHOLD_MM:
            current = current + 1 if prev is not None and (d - prev).days == 1 and current else 1
        else:
            if current:
                lengths.append(current)
            current = 0
        prev = d
        if current and d == max(days):
            lengths.append(current)
    return collections.Counter(lengths)


def report(rain, start, end, label):
    days = [d for d in rain if start <= d <= end]
    selling = [d for d in days if d.weekday() < 6]
    trig_sell = [d for d in selling if rain[d] >= THRESHOLD_MM]
    trig_all = [d for d in days if rain[d] >= THRESHOLD_MM]
    print(f"{label}: {len(trig_sell)} trigger days of {len(selling)} selling days with data; "
          f"{len(trig_all)} of {len(days)} days counting Sundays; runs {dict(sorted(runs(days, rain).items()))}")
    return selling


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "univalle_raw.csv"
    rain = load_days(path)
    selling = report(rain, *WINDOW, "27 sep 2025 to 26 sep 2026")
    by_month = collections.OrderedDict()
    for d in sorted(selling):
        m = by_month.setdefault(d.strftime("%Y-%m"), [0, 0])
        m[0] += 1
        m[1] += rain[d] >= THRESHOLD_MM
    for month, (n, t) in by_month.items():
        print(f"  {month}: {n:>2} selling days with data, {t} trigger days")
    report(rain, dt.date(2025, 1, 1), dt.date(2025, 12, 31), "calendar 2025")


if __name__ == "__main__":
    main()
