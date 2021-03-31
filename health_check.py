from lx16a import *
##Check health of robot

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
left_knee.vInRead()
left_thigh.vInRead()
left_hip.vInRead()

right_knee = LX16A(3)
right_thigh = LX16A(2)
right_hip = LX16A(1)
right_knee.tempRead()
right_thigh.tempRead()
right_hip.tempRead()
right_knee.getPhysicalPos()
right_thigh.getPhysicalPos()
right_hip.getPhysicalPos()
right_knee.vInRead()
right_thigh.vInRead()
rights_hip.vInRead()

