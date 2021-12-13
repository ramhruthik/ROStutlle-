import time
from robot_control_class import RobotControl 
robotcontrol = RobotControl() 

def robotmove(a):
    robotcontrol.move_straight()
    time.sleep(a)
    robotcontrol.stop_robot()

robotmove(5)
