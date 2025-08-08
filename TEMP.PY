import os

folders = [
    "ingest", "detection", "alerting", "dashboard", "terraform", "scripts", "tests", "data/sample_logs"
]
files = [
    "README.md", "requirements.txt", "setup.py", ".gitignore",
    "scripts/run_pipeline.py"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "__init__.py"), "w") as f:
        pass

for file in files:
    open(file, "a").close()

print("Repo structure initialized.")
