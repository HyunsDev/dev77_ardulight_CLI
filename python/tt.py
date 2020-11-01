# def hex_to_rgb(value):
#     value = value.lstrip('#')
#     lv = len(value)
#     return list(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

# a = ""

# testColorSet = ["#ff0000", "#ff6200", "#ff9900", "#ffd500", "#f2ff00", "#a2ff00", "#55ff00", "#00ff77", "#00ffb7", "#00f2ff", "#00aeff", "#0062ff", "#8000ff", "#c300ff", "#ff00fb", "#ff00a6", "#ffffff", "#000000"]

# for i in testColorSet:

#     a = a + ", " + str(hex_to_rgb(i))

# print(a)

# import serial, time, sys
# ser = serial.Serial(port="COM9",baudrate=9600)

# while True:
#     print(ser.writable())
#     if ser.writable():
#         ser.write("1".encode("ascii"))
#         break

import colorsys

def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

i = 0
ii = 0

op = []

while True:
    if i == 18: 
        break
    print()
    op.append(list(hsv2rgb(i*18/360, 1, 1)))
    i = i + 1
print(op)

