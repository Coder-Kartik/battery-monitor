import tkinter as tk

class BatteryMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Battery Level Monitor")
        self.root.geometry("300x250")

        # Create a label for battery percentage
        self.battery_label = tk.Label(root, font=("Helvetica", 24))
        self.battery_label.pack(pady=20)

        # Create a label for battery status
        self.status_label = tk.Label(root, font=("Helvetica", 12))
        self.status_label.pack(pady=10)


