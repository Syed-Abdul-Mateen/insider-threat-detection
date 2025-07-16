# analyzer/behavior_analyzer.py

import os

def analyze_event(alert):
    path = alert["path"]
    event = alert["event"]

    # Define common insider threat indicators
    suspicious_patterns = [
        ".bat", ".ps1", ".sh",  # Script files
        ".zip", ".rar",         # Compressed files
        ".exe", ".dll",         # Executables
    ]

    # Default values
    reason = "Normal activity"
    severity = "low"

    if event == "deleted":
        reason = "Critical file was deleted"
        severity = "medium"

    elif event == "modified":
        reason = "File was modified"
        severity = "low"

    elif event == "created":
        _, ext = os.path.splitext(path)
        if ext.lower() in suspicious_patterns:
            reason = f"Suspicious file type created: {ext}"
            severity = "high"
        else:
            reason = "New file was created"
            severity = "low"

    elif event == "renamed":
        reason = "File was renamed"
        severity = "low"

    # Append reason and severity to the alert
    alert["reason"] = reason
    alert["severity"] = severity
    return alert
