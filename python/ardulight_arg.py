from ardulight import *
import sys

port = sys.argv[1]
command = sys.argv[2]

# f = open('console_arg.log', 'a')
# sys.stdout = f

try:
    a = ardu(port)
    eval(f"a.{command}")
    a.close()
except Exception as e:
    print(e)
