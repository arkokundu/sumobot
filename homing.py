from lx16a import *
from math import sin, cos

LX16A.initialize('/dev/ttyUSB0')

#ID = LX16A.IDRead()
servo1 = LX16A(8)

servo1.moveTimeWrite(120) #moves servo to home position 
