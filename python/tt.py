# def hex_to_rgb(value):
#     value = value.lstrip('#')
#     lv = len(value)
#     return list(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

# a = ""

# testColorSet = ["#ff0000", "#ff6200", "#ff9900", "#ffd500", "#f2ff00", "#a2ff00", "#55ff00", "#00ff77", "#00ffb7", "#00f2ff", "#00aeff", "#0062ff", "#8000ff", "#c300ff", "#ff00fb", "#ff00a6", "#ffffff", "#000000"]

# for i in testColorSet:

#     a = a + ", " + str(hex_to_rgb(i))

# print(a)

import serial, time, sys
ser = serial.Serial(port="COM9",baudrate=9600)

while True:
    print(ser.writable())
    if ser.writable():
        ser.write("1".encode("ascii"))
        break