import threading
import time
from gui import LoggerGUI
from process_manager import EventMonitor
import tkinter as tk

class Application:
    def __init__(self, master):
        self.gui = LoggerGUI(master)
        self.event_monitor = EventMonitor(self.gui.log_event)

    def start_monitoring(self):
        monitoring_thread = threading.Thread(target=self.event_monitor.monitor)
        monitoring_thread.daemon = True
        monitoring_thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    app.start_monitoring()
    root.mainloop()