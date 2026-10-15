import json

def lambda_handler(event, context):
    """
    Minimal AWS Lambda demonstration.
    Accepts JSON with `readings` as a list of numbers (kWh).
    This does not replace the full Glue/Step Functions/Athena pipeline.
    """
    readings = event.get("readings", [])
    clean = []
    for value in readings:
        try:
            number = float(value)
            if number >= 0:
                clean.append(number)
        except (TypeError, ValueError):
            continue

    total = round(sum(clean), 2)
    average = round(total / len(clean), 2) if clean else 0
    return {
        "statusCode": 200,
        "body": json.dumps({
            "valid_reading_count": len(clean),
            "total_kwh": total,
            "average_kwh": average,
            "note": "Demo processing only; no live meter or EB tariff connection."
        })
    }
