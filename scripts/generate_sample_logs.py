import os
import json
import random
from datetime import datetime, timedelta

# Ensure folder exists
os.makedirs("data/sample_logs", exist_ok=True)

# Sample values to randomize
usernames = ["alice", "bob", "charlie", "admin"]
sources = ["ec2.amazonaws.com", "s3.amazonaws.com", "iam.amazonaws.com"]
actions = ["StartInstances", "StopInstances", "CreateBucket", "DeleteUser"]
regions = ["us-east-1", "us-west-2", "eu-central-1"]
user_agents = ["aws-cli/1.16.220", "console.amazonaws.com", "terraform/1.5.0"]
ips = ["192.168.1.10", "203.0.113.45", "52.95.110.1", "18.232.34.12"]

# Generate N files with M records each
num_files = 5
events_per_file = 10

for i in range(num_files):
    records = []
    for _ in range(events_per_file):
        timestamp = datetime.utcnow() - timedelta(minutes=random.randint(0, 1440))
        record = {
            "eventVersion": "1.08",
            "userIdentity": {
                "type": "IAMUser",
                "userName": random.choice(usernames)
            },
            "eventTime": timestamp.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "eventSource": random.choice(sources),
            "eventName": random.choice(actions),
            "awsRegion": random.choice(regions),
            "sourceIPAddress": random.choice(ips),
            "userAgent": random.choice(user_agents),
            "requestParameters": {
                "instancesSet": {
                    "items": [{"instanceId": f"i-{random.randint(10000000, 99999999)}"}]
                }
            },
            "responseElements": None
        }
        records.append(record)

    with open(f"data/sample_logs/cloudtrail_sample_{i + 1}.json", "w") as f:
        json.dump({"Records": records}, f, indent=2)

print("✅ Sample CloudTrail logs created in data/sample_logs/")
