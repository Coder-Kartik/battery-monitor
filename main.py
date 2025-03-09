import tkinter as tk
from battery_gui import BatteryMonitorApp
from battery_refresh import update_battery_status

root = tk.Tk()
app = BatteryMonitorApp(root)

# Call the function to update battery status initially
update_battery_status(app)

root.mainloop()
