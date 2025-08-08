# 🔐 AI-Powered Cloud Threat Detection System

A lightweight threat detection pipeline that ingests AWS CloudTrail-style logs, applies machine learning to detect suspicious activity, and visualizes the results via a Streamlit dashboard.

Accessible via the link below:
https://cloud-threat-detector.streamlit.app/

---

## 🚀 Features

- Ingests structured (mocked or real) AWS CloudTrail logs
- Uses Isolation Forest to detect anomalies in user/API activity
- Streamlit dashboard for log exploration and filtering
- Console-based alerts for flagged events (Slack/email-ready)
- Ready for AWS S3, CloudTrail, Terraform-based deployment (optional)

---

## 💻 How to Run Locally

```bash
# 1. Clone and enter
git clone https://github.com/yourname/cloud-threat-detector.git
cd cloud-threat-detector

# 2. Set up environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Generate mock logs
python scripts/generate_sample_logs.py

# 4. Run detection
python -m scripts.run_pipeline

# 5. Launch dashboard
streamlit run dashboard/app.py
```

---

## Anomaly Detection Logic

Model: IsolationForest

Features: user, action, ip, region, timestamp (hour/day), source, userAgent

Output: Anomaly score + binary anomaly flag (is_anomaly)

---

## TODO (Next Steps)

Add email/Slack alerting

Export anomalies to CSV

Deploy to Streamlit Cloud

---

## Credits

Built by Tanish Bollam for learning, demo, and resume use.
Inspired by real-world Security Information and Event Management (SIEM) pipelines.
