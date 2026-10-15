"""
Smart EB Guardian - simple local prototype
Run: python python/analyze_data.py
Uses only Python's standard library.
The readings are synthetic demo data, not actual EB meter readings.
"""
import csv, json, os
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "electricity_readings.csv")
OUT = os.path.join(ROOT, "data", "dashboard_summary.json")

daily = defaultdict(float)
monthly = defaultdict(float)
floor_total = defaultdict(float)
all_values = []

with open(DATA, newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        date = row["date"]
        floor = row["floor"]
        kwh = float(row["consumption_kwh"])
        daily[date] += kwh
        monthly[date[:7]] += kwh
        floor_total[floor] += kwh
        all_values.append({"date": date, "floor": floor, "kwh": kwh})

# Simple transparent baseline: estimated bill = total kWh * assumed sample tariff.
# Replace 7.5 with the tariff relevant to your assignment; actual EB slabs vary.
tariff = 7.50
total_kwh = sum(daily.values())
daily_values = list(daily.values())
avg_daily = total_kwh / max(len(daily_values), 1)
forecast_month_kwh = avg_daily * 30
forecast_bill = forecast_month_kwh * tariff

# Simple anomaly flag: daily total > average + 2 standard deviations
mean = avg_daily
variance = sum((x - mean) ** 2 for x in daily_values) / max(len(daily_values), 1)
std = variance ** 0.5
alerts = []
for date, value in sorted(daily.items()):
    if std > 0 and value > mean + 1.4 * std:
        alerts.append({"date": date, "consumption_kwh": round(value, 2),
                       "reason": "Usage is higher than the normal daily pattern"})

summary = {
    "demo_data": True,
    "tariff_inr_per_kwh": tariff,
    "total_consumption_kwh": round(total_kwh, 2),
    "average_daily_kwh": round(avg_daily, 2),
    "forecast_next_30_days_kwh": round(forecast_month_kwh, 2),
    "estimated_bill_inr": round(forecast_bill, 2),
    "monthly_consumption_kwh": {k: round(v, 2) for k, v in sorted(monthly.items())},
    "floor_consumption_kwh": {k: round(v, 2) for k, v in sorted(floor_total.items())},
    "daily_consumption_kwh": {k: round(v, 2) for k, v in sorted(daily.items())},
    "anomaly_alerts": alerts[:10],
}
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2)
print("Analysis completed.")
print(f"Total demo consumption: {summary['total_consumption_kwh']} kWh")
print(f"Estimated next-30-day bill: Rs. {summary['estimated_bill_inr']}")
print(f"Potential anomaly alerts: {len(summary['anomaly_alerts'])}")
print(f"Saved: {OUT}")
