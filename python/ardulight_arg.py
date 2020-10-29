from ardulight import *
import sys

port = sys.argv[1]
command = sys.argv[2]

a = ardu(port)
eval(f"a.{command}")