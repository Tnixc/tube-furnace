# main.py for ESP32 (MicroPython)

import time

counter = 0

while True:
    msg = "hello from esp32: {}".format(counter)
    print(msg)  # goes to usb serial, can be read by desktop
    counter += 1
    time.sleep(1)  # wait 1 second
