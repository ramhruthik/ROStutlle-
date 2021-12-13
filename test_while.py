import time
from robot_control_class import RobotControl 
robotcontrol = RobotControl() 

laser1 = robotcontrol.get_laser(360)

while laser1 > 1:
    robotcontrol.move_straight()
    laser1 = robotcontrol.get_laser(360)
    print("distance: ", laser1)

robotcontrol.stop_robot()
print(" I'm off the wall: ")
