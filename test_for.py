from robot_control_class import RobotControl 
robotcontrol = RobotControl() 

laser = robotcontrol.get_laser_full()

lower_value = 10000
for value in laser:
 
    if value < lower_value:
        lower_value = value
print("The lower_value is: ",lower_value)
