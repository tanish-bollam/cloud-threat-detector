from ingest.cloudtrail_ingest import load_logs_from_folder
from detection.model import ThreatDetector
from alerting.notifier import print_alerts

# Step 1: Load logs
df = load_logs_from_folder("data/sample_logs")

# Step 2: Initialize + train
detector = ThreatDetector()
detector.fit(df)

# Step 3: Predict anomalies
result_df = detector.predict(df)

# Step 4: Print alerts
print_alerts(result_df)
