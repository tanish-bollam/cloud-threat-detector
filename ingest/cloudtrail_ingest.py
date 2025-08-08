import os
import json
import pandas as pd

def load_logs_from_folder(folder_path):
    records = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            with open(os.path.join(folder_path, filename)) as f:
                try:
                    data = json.load(f)
                    for record in data.get("Records", []):
                        records.append(parse_record(record))
                except Exception as e:
                    print(f"Error parsing {filename}: {e}")
    return pd.DataFrame(records)

def parse_record(r):
    return {
        "timestamp": r.get("eventTime"),
        "user": r.get("userIdentity", {}).get("userName"),
        "source": r.get("eventSource"),
        "action": r.get("eventName"),
        "region": r.get("awsRegion"),
        "ip": r.get("sourceIPAddress"),
        "userAgent": r.get("userAgent")
    }

if __name__ == "__main__":
    df = load_logs_from_folder("data/sample_logs")
    print(df.head())
