import serial, time

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

class ardu:
    def __init__(self, port):
        self.port = port
        self.ser = serial.Serial(
        port=port,
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=0)
    
    def on(self):
        self.ser.write(b'0')
        print(f"[{self.port}] 0")

    def off(self):
        self.ser.write(b'1')
        print(f"[{self.port}] 1")

    def soild(self, color:list):
        self.ser.write(f'2 0 {color[0]} {color[1]} {color[2]}'.encode("ascii"))
        print(f"[{self.port}] 2 0 {color[0]} {color[1]} {color[2]}")

    def each(self, colors:list):
        color_list = ""
        for color in colors:
            color_list += f" {color[0]} {color[1]} {color[2]}"

        self.ser.write(f"3 0 {color_list}".encode("ascii"))
        print(f"[{self.port}] 3 0{color_list}")

    def spac(self, delay, colors):
        color_list = ""
        for color in colors:
            color_list += f" {color[0]} {color[1]} {color[2]}"

        self.ser.write(f"4 {str(delay)}{color_list}".encode("ascii"))
        print(f"[{self.port}] 4 {str(delay)}{color_list}")


    def breath(self, delay, color):
        # self.ser.write(f"5 {str(delay)} {color[0]} {color[1]} {color[2]}".encode("ascii"))
        # print(f"[{self.port}] 5 {str(delay)} {color[0]} {color[1]} {color[2]}")
        print("Can't Use")

    def wave(self, delay:int, colors:list):
        color_list = ""
        for color in colors:
            color_list += f" {color[0]} {color[1]} {color[2]}"

        self.ser.write(f"6 {str(delay)}{color_list}".encode("ascii"))
        print(f"[{self.port}] 6 {str(delay)}{color_list}")

    def down(self, delay:int, color:list):
        self.ser.write(f'7 {str(delay)} {color[0]} {color[1]} {color[2]}'.encode("ascii"))
        print(f"[{self.port}] 7 {str(delay)} {color[0]} {color[1]} {color[2]}")

    def wipe(self, delay:int, colors:list):
        color_list = ""
        for color in colors:
            color_list += f" {color[0]} {color[1]} {color[2]}"

        self.ser.write(f"8 {str(delay)}{color_list}".encode("ascii"))
        print(f"[{self.port}] 8 {str(delay)}{color_list}")

    def raw(self, command:str):
        self.ser.write(f"{command}".encode("ascii"))
        print(f"[{self.port}] {command}")