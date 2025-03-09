from battery_status import get_battery_status

def update_battery_status(app):
    battery_percentage, plugged = get_battery_status()

    if battery_percentage is not None:
        app.battery_label.config(text=f"Battery: {battery_percentage}%")
        if plugged:
            app.status_label.config(text="Status: Plugged In", fg="green")
        else:
            app.status_label.config(text="Status: Running on Battery", fg="red")
    else:
        app.battery_label.config(text="Battery status not available")
        app.status_label.config(text="", fg="black")
