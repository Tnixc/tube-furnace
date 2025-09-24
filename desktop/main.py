import serial

ser = serial.Serial("/dev/cu.usbserial-1130", 115200)

while True:
    line = ser.readline().decode().strip()
    print("from esp32:", line)
