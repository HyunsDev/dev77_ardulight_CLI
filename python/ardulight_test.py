from ardulight import * 
import time

# testColorSet = ["#ff0000", "#ff6200", "#ff9900", "#ffd500", "#f2ff00", "#a2ff00", "#55ff00", "#00ff77", "#00ffb7", "#00f2ff", "#00aeff", "#0062ff", "#8000ff", "#c300ff", "#ff00fb", "#ff00a6", "#ffffff", "#000000"]
testColorlist = [[255, 0, 0], [255, 98, 0], [255, 153, 0], [255, 213, 0], [242, 255, 0], [162, 255, 0], [85, 255, 0], [0, 255, 119], [0, 255, 183], [0, 242, 255], [0, 174, 255], [0, 98, 255], [128, 0, 255], [195, 0, 255], [255, 0, 251], [255, 0, 166], [255, 255, 255], [0, 0, 0]]

test_time = 2


a = ardu("COM9")

print(f"==========[Ardulight Test Code]==========")

# ON
print("\n[1/9] on")
a.on()

# OFF
time.sleep(test_time)
print("\n[2/9] off")
a.off()

# soild
time.sleep(test_time)
print("\n[3/9] soild")
a.soild([255, 255, 0])

# each
time.sleep(test_time)
print("\n[4/9] each")
a.each(testColorlist)

# spac
time.sleep(test_time)
print("\n[5/9] spac")
a.spac(300, testColorlist)

# breath
time.sleep(test_time)
print("\n[6/9] breath")
a.breath(300, [255, 255, 0])

# wave
time.sleep(test_time)
print("\n[7/9] wave")
a.wave(300, testColorlist)

# down
time.sleep(test_time)
print("\n[8/9] down")
a.down(300, [255, 255, 0])

# wipe
time.sleep(test_time)
print("\n[9/9] wipe")
a.wipe(300, testColorlist)

print("\nEND")