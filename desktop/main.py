import serial
from common.schema import StateMessage

ser = serial.Serial("/dev/cu.usbserial-1130", 115200)

while True:
    line = ser.decode()
    print("from esp32:", line)
