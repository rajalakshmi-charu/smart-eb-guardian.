# Smart EB Guardian — one-day starter prototype

## What this starter kit contains
- `data/electricity_readings.csv`: synthetic daily readings for 5 areas over 30 days.
- `python/analyze_data.py`: local Python summary, simple bill estimate and anomaly flags.
- `dashboard/index.html`: a self-contained dashboard with charts, bill estimate, anomaly table and demo Q&A.
- `screenshots/`: dashboard images for report placeholders.
- `aws/`: a simple Lambda example and deployment checklist.

## Important truth-in-reporting note
The included dashboard and screenshots are a **local prototype using synthetic data**. They are not screenshots of a deployed AWS environment. The chatbot is rule-based demo Q&A, not a live Amazon Bedrock RAG integration. Do not describe AWS services as deployed until you actually create and test them. You can use these as prototype UI screenshots and replace them with real AWS screenshots after deployment.

## Start in 5 steps
1. Extract this ZIP to a folder such as `Desktop/Smart_EB_Guardian`.
2. Install Python 3 if needed and open the folder in VS Code.
3. Open a terminal in VS Code.
4. Run `python python/analyze_data.py` (Windows may use `py python/analyze_data.py`).
5. Double-click `dashboard/index.html` to open the dashboard in a browser.

No extra Python packages are required for `analyze_data.py`.

## One-day build order
1. Run the Python analysis and confirm it writes `data/dashboard_summary.json`.
2. Open the dashboard and capture screenshots.
3. In AWS Console, create an S3 bucket in your preferred region, keep public access blocked, and upload the CSV. Check AWS billing before creating resources.
4. If time permits, create a Lambda function from `aws/lambda_handler.py` and test it with the included sample JSON. This is only a small serverless processing demo.
5. Only claim the AWS integration that you have actually tested. A full Glue/Step Functions/Athena/Bedrock RAG deployment is not realistic to guarantee in one day for a beginner.

## Screenshots for report
- `screenshots/figure_4_28_dashboard.png`: dashboard overview, floor consumption and forecast.
- `screenshots/figure_4_29_anomaly_alerts.png`: anomaly alerts section.
- `screenshots/figure_4_30_chat_assistant.png`: demo Q&A section.

Suggested captions, adjusted to reflect the prototype:
- Figure 4.28: Smart EB Guardian prototype dashboard showing sample consumption by area and estimated bill.
- Figure 4.29: Prototype anomaly alert list based on synthetic electricity readings.
- Figure 4.30: Example rule-based assistant response; live RAG integration is future work unless implemented.

## Bill estimate
The sample tariff is Rs. 7.50/kWh and is only an illustrative constant. Replace it with an appropriate sample tariff for your report; actual electricity bills may use slabs, fixed charges, taxes and other adjustments.
