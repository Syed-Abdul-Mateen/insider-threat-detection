# logger/activity_logger.py

import json
import os

LOG_FILE = "activity_log.json"

def log_activity(alert):
    # Create the log file if it doesn't exist
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([], f, indent=4)

    # Read existing log entries
    with open(LOG_FILE, "r") as f:
        try:
            logs = json.load(f)
        except json.JSONDecodeError:
            logs = []

    # Append the new alert
    logs.append(alert)

    # Write the updated log back to file
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)
