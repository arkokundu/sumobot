from lx16a import *
from math import sin, cos

LX16A.initialize('/dev/ttyUSB0')

servo1 = LX16A(8)
servo2 = LX16A(7)

t = 0

while True:
    servo1.moveTimeWrite(120+sin(t)*50)
    servo2.moveTimeWrite(120+cos(t)*50)
    t+=0.01