import psutil

import time
import csv
import os

class EventMonitor:
    def __init__(self, log_event_callback):
        self.log_event_callback = log_event_callback
        self.log_file = "security_events.csv"
        self.create_log_file()

    def create_log_file(self):
        if not os.path.exists(self.log_file):
            with open(self.log_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Timestamp", "Event"])

    def log_event(self, event):
        with open(self.log_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(event)

    def monitor(self):
        while True:
            # Monitor for unauthorized access attempts or suspicious processes
            for proc in psutil.process_iter(['pid', 'name', 'username']):
                try:
                    if proc.info['username'] != 'your_username':  # Replace with your username
                        event = (time.strftime("%Y-%m-%d %H:%M:%S"), f"Suspicious process detected: {proc.info['name']} (PID: {proc.info['pid']})")
                        self.log_event(event)
                        self.log_event_callback(event[1])
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
            time.sleep(5)  # Adjust the sleep time as needed