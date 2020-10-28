import serial, time

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

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

    def soild(self, color:str):
        color = hex_to_rgb(color)

        self.ser.write(b'2')
        print(f"[{self.port}] 2 0 {color[0]} {color[1]} {color[2]}")

    def each(self, colors:list):
        color_list = ""
        for color in colors:
            color = hex_to_rgb(color)
            color_list += f" {color[0]} {color[1]} {color[2]}"

        self.ser.write(f"3 {color_list}".encode("ascii"))
        print(f"[{self.port}] 3 0{color_list}")

    def spac(self, delay, colors):
        if str(type(colors)) == "<class 'list'>":
            color_list = ""
            for color in colors:
                color = hex_to_rgb(color)
                color_list += f" {color[0]} {color[1]} {color[2]}"

            self.ser.write(f"4 {str(delay)}{color_list}".encode("ascii"))
            print(f"[{self.port}] 4 {str(delay)}{color_list}")

        else:
            print("추가설정필요")

    def breath(self, delay, color):
        color = hex_to_rgb(color)
        self.ser.write(f"5 {str(delay)} {color[0]} {color[1]} {color[2]}".encode("ascii"))
        print(f"[{self.port}] 5 {str(delay)} {color[0]} {color[1]} {color[2]}")
        
    def wave(self, delay, colors):
        if str(type(colors)) == "<class 'list'>":
            color_list = ""
            for color in colors:
                color = hex_to_rgb(color)
                color_list += f" {color[0]} {color[1]} {color[2]}"

            self.ser.write(f"6 {str(delay)}{color_list}".encode("ascii"))
            print(f"[{self.port}] 6 {str(delay)}{color_list}")

        else:
            print("추가설정필요")

    def clear(self):
        self.ser.write(f"clear".encode("ascii"))



if __name__ == "__main__":
    testColorSet = ["#ff0000", "#ff6200", "#ff9900", "#ffd500", "#f2ff00", "#a2ff00", "#55ff00", "#00ff77", "#00ffb7", "#00f2ff", "#00aeff", "#0062ff", "#8000ff", "#c300ff", "#ff00fb", "#ff00a6", "#ffffff", "#000000"]
    a = ardu("COM9")

    print(f"==========[Ardulight Test Code]==========")

    # ON
    print("\n[1/7] on")
    a.on()

    # OFF
    time.sleep(3)
    print("\n[2/7] off")
    a.off()

    # soild
    time.sleep(3)
    print("\n[3/7] soild")
    a.soild("ffffff")

    # each
    time.sleep(3)
    print("\n[4/7] each")
    a.each(testColorSet)

    # spac
    time.sleep(3)
    print("\n[5/7] spac")
    a.spac(300, testColorSet)

    # breath
    time.sleep(3)
    print("\n[6/7] breath")
    a.breath(300, "#668fc4")

    # wave
    time.sleep(3)
    print("\n[7/7] wave")
    a.wave(300, testColorSet)

    print("\nEND")