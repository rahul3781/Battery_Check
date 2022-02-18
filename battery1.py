import psutil
from plyer import notification
import time

# from psutil we will import the
# sensors_battery class and with
# that we have the battery remaining
while True :
    battery = psutil.sensors_battery()
    percent = battery.percent
    plugged = battery.power_plugged
    if plugged:
        if percent > 80:
            notification.notify(
                title="Plug Out",
                message=str(percent) + "% Battery remaining",
                timeout=2
            )
    if not plugged:
        if percent < 20:
            notification.notify(
                title="Plug In",
                message=str(percent) + "% Battery remaining",
                timeout=2
            )
    # after every 60 mins it will show the
    # battery percentage
    time.sleep(60 * 60)

    continue