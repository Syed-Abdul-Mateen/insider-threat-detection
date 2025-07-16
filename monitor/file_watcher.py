# monitor/file_watcher.py

import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class InsiderThreatFileWatcher(FileSystemEventHandler):
    def __init__(self, watch_dir, callback=None):
        self.watch_dir = watch_dir
        self.callback = callback

    def on_modified(self, event):
        if not event.is_directory:
            self.report_event("modified", event.src_path)

    def on_created(self, event):
        if not event.is_directory:
            self.report_event("created", event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            self.report_event("deleted", event.src_path)

    def on_moved(self, event):
        if not event.is_directory:
            self.report_event("renamed", f"{event.src_path} -> {event.dest_path}")

    def report_event(self, event_type, file_path):
        raw_alert = {
            "event": event_type,
            "path": file_path,
            "timestamp": time.ctime()
        }
        if self.callback:
            self.callback(raw_alert)

def start_watching(directory, callback=None):
    event_handler = InsiderThreatFileWatcher(directory, callback=callback)
    observer = Observer()
    observer.schedule(event_handler, path=directory, recursive=True)
    observer.start()
    print(f"[+] Monitoring directory: {directory}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
