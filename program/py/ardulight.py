import serial, time, sys

class ardu:
    def __init__(self, port):
        self.port = port
        self.ser = serial.Serial(port, 9600)
        time.sleep(2)

    def save(self, content):
        print(content)
        with open("log.log", "a") as f:
            f.write(content + "\n")

    def on(self):
        self.ser.write(b'9')
        self.save(f"[{self.port}] 9")
        time.sleep(1)

    def off(self):
        self.ser.write(b'1')
        self.save(f"[{self.port}] 1")
        time.sleep(1)

    def soild(self, color:list):
        self.ser.write(f'2 0 {color[0]} {color[1]} {color[2]}'.encode("ascii"))
        self.save(f"[{self.port}] 2 0 {color[0]} {color[1]} {color[2]}")
        time.sleep(1)

    def each(self, colors:list):
        color_list = ""
        for color in colors:
            color_list += f" {color[0]} {color[1]} {color[2]}"

        self.ser.write(f"3 0 {color_list}".encode("ascii"))
        self.save(f"[{self.port}] 3 0{color_list}")
        time.sleep(1)

    def spac(self, delay):
        self.ser.write(f"4 {str(delay)}".encode("ascii"))
        self.save(f"[{self.port}] 4 {str(delay)}")
        time.sleep(1)


    def wave(self, delay:int, colors:list):
        color_list = ""
        for color in colors:
            color_list += f" {color[0]} {color[1]} {color[2]}"

        self.ser.write(f"6 {str(delay)}{color_list}".encode("ascii"))
        
        self.save(f"[{self.port}] 6 {str(delay)}{color_list}")
        time.sleep(1)

    def down(self, delay:int, color:list):
        self.ser.write(f'7 {str(delay)} {color[0]} {color[1]} {color[2]}'.encode("utf-8"))
        
        self.save(f"[{self.port}] 7 {str(delay)} {color[0]} {color[1]} {color[2]}")
        time.sleep(1)
        
    def wipe(self, delay:int, colors:list):
        color_list = ""
        for color in colors:
            color_list += f" {color[0]} {color[1]} {color[2]}"

        self.ser.write(f"8 {str(delay)}{color_list}".encode("ascii"))
        
        self.save(f"[{self.port}] 8 {str(delay)}{color_list}")
        time.sleep(1)

    def raw(self, command:str):
        self.ser.write(f"{command}".encode("utf-8"))

        # print(f"{command}".encode("ascii"))
        self.save(f"[{self.port}] {command}")
        time.sleep(1)

    def readline(self):
        return self.ser.readline()
        

    def close(self):
        self.ser.close()

if __name__ == "__main__":
    a = ardu("COM15")
    a.raw("7 30 255 255 255")
