import tkinter as tk
from battery_gui import BatteryMonitorApp
from battery_refresh import update_battery_status

def refresh_battery_status():
    update_battery_status(app)  # Update the battery status
    root.after(5000, refresh_battery_status)  # Call again after 5 seconds

root = tk.Tk()
app = BatteryMonitorApp(root)

# Call the function initially and then schedule periodic updates
refresh_battery_status()

root.mainloop()
