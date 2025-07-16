# main.py

import os
import time
from monitor.file_watcher import start_watching
from analyzer.behavior_analyzer import analyze_event
from logger.activity_logger import log_activity

def handle_alert(raw_alert):
    enriched_alert = analyze_event(raw_alert)

    print("\n[!] Potential Insider Threat Detected:")
    print(f"    - Path: {enriched_alert['path']}")
    print(f"    - Event: {enriched_alert['event']}")
    print(f"    - Reason: {enriched_alert['reason']}")
    print(f"    - Severity: {enriched_alert['severity']}")
    print(f"    - Time: {enriched_alert['timestamp']}")

    log_activity(enriched_alert)

if __name__ == "__main__":
    print("=== Behavior-Based Insider Threat Detection System ===\n")

    # Define the directory to watch
    watch_dir = os.path.join(os.getcwd(), "sample_watch_dir")

    # Create the folder if it doesn't exist
    if not os.path.exists(watch_dir):
        os.makedirs(watch_dir)

    print(f"[+] Watching directory: {watch_dir}\n")
    start_watching(watch_dir, callback=handle_alert)
