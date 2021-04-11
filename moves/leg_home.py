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

left_knee.moveTimeWrite(88,time=1000)
left_thigh.moveTimeWrite(140,time=1000)
right_knee.moveTimeWrite(164,time=1000)
right_thigh.moveTimeWrite(97,time=1000)
