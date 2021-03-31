from lx16a import *
##Shutdown robot - Put it in sleep position

LX16A.initialize('/dev/ttyUSB1')

left_knee = LX16A(8)
left_thigh = LX16A(7)
left_hip = LX16A(6)
left_knee.tempRead()
left_thigh.tempRead()
left_hip.tempRead()
left_knee.getPhysicalPos()
left_thigh.getPhysicalPos()
left_hip.getPhysicalPos()

#Moves Left Leg to home position slowly

left_knee.moveTimeWrite(120,time=2000)
left_thigh.moveTimeWrite(120,time=2000)
left_hip.moveTimeWrite(120,time=2000)

right_knee = LX16A(3)
right_thigh = LX16A(2)
right_hip = LX16A(1)
right_knee.tempRead()
right_thigh.tempRead()
right_hip.tempRead()
right_knee.getPhysicalPos()
right_thigh.getPhysicalPos()
right_hip.getPhysicalPos()

#Moves Right Leg to home position slowly
right_knee.moveTimeWrite(120,time=2000)
right_thigh.moveTimeWrite(120,time=2000)
right_hip.moveTimeWrite(120,time=2000)
