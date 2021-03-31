from lx16a import *
from math import sin, cos
import time

LX16A.initialize('/dev/ttyUSB1')


left_knee = LX16A(8)
left_thigh = LX16A(7)
left_hip = LX16A(6)
right_knee = LX16A(3)
right_thigh = LX16A(2)
right_hip = LX16A(1)
print(left_knee.getPhysicalPos())
print(left_thigh.getPhysicalPos())
print(right_knee.getPhysicalPos())
print(right_thigh.getPhysicalPos())

#left_leg.moveTimeWriteRel(10, 3000)
#time.sleep(1)
#right_leg.moveTimeWriteRel(10, 3000)

#right_leg.moveTimeWriteRel(10,2000)
#left_kne.moveTimeWriteRel(10,2000)

right_knee.moveTimeWrite(120,time=2000)
left_knee.moveTimeWrite(120,time=2000)
right_thigh.moveTimeWrite(120,time=2000)
left_thigh.moveTimeWrite(120,time=2000)

#t = 0

#while True:
#    right_thigh.moveTimeWriteRel(sin(t)*20, time=20)
#    left_thigh.moveTimeWriteRel(cos(t)*20, time=20)
#    t+=10