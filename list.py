from robot_control_class import RobotControl
robotcontrol = RobotControl() 

laser = robotcontrol.get_laser_full()

print ("Position: 0", laser[0])
print ("Position: 360", laser[360])
print ("Position: 719", laser[719])
