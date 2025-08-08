def print_alerts(df):
    print("\n🚨 ANOMALY ALERTS DETECTED 🚨\n")

    if df.empty or "is_anomaly" not in df.columns:
        print("No data to alert on.")
        return

    flagged = df[df["is_anomaly"] == 1]

    if flagged.empty:
        print("✅ No anomalies detected.")
        return

    for _, row in flagged.iterrows():
        print(f"""
-------------------------
🔒 Suspicious Activity Detected
-------------------------
Timestamp    : {row['timestamp']}
User         : {row['user']}
Region       : {row['region']}
Source       : {row['source']}
Action       : {row['action']}
Address      : {row['ip']}
Score        : {row['anomaly_score']:.4f}
-------------------------
""")
