# Optional AWS quick-start checklist (do only after local demo works)

1. Sign in to AWS Console and check Billing. Set a budget alert; a budget alert is not a hard spending cap.
2. Choose a region and create an S3 bucket with Block Public Access enabled.
3. Upload `data/electricity_readings.csv` to the bucket.
4. Open Lambda, create a Python runtime function, paste `aws/lambda_handler.py`, deploy and test.
5. Use a test event such as:
   {"readings": [12.5, 15, 13.2, -1, "bad", 18]}
6. Confirm the response returns valid_reading_count, total_kwh and average_kwh.
7. Capture a real screenshot of the S3 object and Lambda test response for the report.
8. Do not expose AWS keys in code or make the S3 bucket public for this prototype.

A true API Gateway + Lambda + S3 + Glue + Athena + Step Functions + Bedrock RAG integration is a larger build. Add those only if you have sufficient time and can test them.
