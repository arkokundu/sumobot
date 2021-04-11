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

print("Left knee : " , left_knee.getPhysicalPos())
print("Left thigh : " , left_thigh.getPhysicalPos())
print("Right Knee : " , right_knee.getPhysicalPos())
print("Right Thigh : " , right_thigh.getPhysicalPos())
print(" Left Hand : " , left_hand.getPhysicalPos())
print("Left Hip : " , left_hip.getPhysicalPos())
print("Right hand : " , right_hand.getPhysicalPos())
print("Right hip : " , right_hip.getPhysicalPos())
