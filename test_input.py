from robot_control_class import RobotControl 
robotcontrol = RobotControl() 

position = input("What's the angle position? ")

laser1 = robotcontrol.get_laser(position)

print ("The laser value received is: ", laser1)
