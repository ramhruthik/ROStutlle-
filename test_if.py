from robot_control_class import RobotControl 
robotcontrol = RobotControl() 

laser = robotcontrol.get_laser(360)
print(laser)

if laser <= 1:
    robotcontrol.stop_robot()

else:
    robotcontrol.move_straight()

print_reading()
