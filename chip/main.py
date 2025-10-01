# main.py for ESP32 (MicroPython)

import time
import sys
from schema import StateMessage
counter = 0

while True:
    msg_obj = StateMessage(t_seconds=counter,temp_c=1.2,slope=1.3)
    sys.stdout.buffer.write(msg_obj.encode())  # goes to usb serial, can be read by desktop
    sys.stdout.flush()
    time.sleep(1)  # wait 1 second
