from lx16a import *
from math import sin, cos
import time

LX16A.initialize('/dev/ttyUSB0')


left_knee = LX16A(8)
left_thigh = LX16A(7)
left_hip = LX16A(6)
right_knee = LX16A(3)
right_thigh = LX16A(2)
right_hip = LX16A(1)
right_hand = LX16A(4)
left_hand = LX16A(5)

left_hand.moveTimeWrite(160,time=1000)
right_hand.moveTimeWrite(100,time=1000)
time.sleep(1)

t = 0
while True:
    right_hand.moveTimeWrite(100+sin(t)*50)
    left_hand.moveTimeWrite(160+sin(t)*50)
    t += 0.005

#left_hand.moveTimeWrite(100, time=1000)
#right_hand.moveTimeWriteRel(20,time=2000)
#left_hand.moveTimeWriteRel(20,time=2000)

