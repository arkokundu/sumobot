from lx16a import *
from math import sin, cos

LX16A.initialize('/dev/ttyUSB0')

left_leg = LX16A(8)
left_knee = LX16A(7)
right_leg = LX16A(3)
right_knee = LX16A(2)

pos1 = left_leg.getPhysicalPos()
print("The left leg motor physical position is {} degrees".format(pos1))
print("The left leg motor temperature (in deg C) is {}".format(left_leg.tempRead()))

pos2 = left_knee.getPhysicalPos()
print("The left knee motor physical position is {} degrees".format(pos2))
print("The left knee motor temperature (in deg C) is {}".format(left_knee.tempRead()))

pos3 = right_leg.getPhysicalPos() 
print("The right leg motor physical position is {} degrees".format(pos3))
print("The right leg motor temperature (in deg C) is {}".format(right_leg.tempRead()))

pos4 = right_knee.getPhysicalPos()
print("The right knee motor physical position is {} degrees".format(pos4))
print("The right knee motor temperature (in deg C) is {}".format(right_knee.tempRead()))



