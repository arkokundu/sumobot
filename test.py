from lx16a import *
from math import sin, cos

LX16A.initialize('/dev/ttyUSB0')

servo1 = LX16A(8)
servo2 = LX16A(7)

pos1 = servo1.getPhysicalPos()
print("The servo's physical position is {} degrees".format(pos1))

pos2 = servo2.getPhysicalPos()
print("The servo's physical position is {} degrees".format(pos2))