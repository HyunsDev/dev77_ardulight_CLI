import serial, time, sys

ser = serial.Serial("COM15", 9600)
time.sleep(2)

i = 0
d = 20

cl = [255, 255 ,255]

command = "7 30 255 255 255"
while True:
    print(ser.readline())
    i = i + 1
    if i == 2:
        ser.write(f"{command}".encode("utf-8"))
        time.sleep(1)


# ser.write(f"{command}".encode("utf-8"))