import time
from robot_control_class import RobotControl #importa uma classe
robotcontrol = RobotControl() #criando um objeto

def robotmove(a):
    robotcontrol.move_straight()
    time.sleep(a)
    robotcontrol.stop_robot()

print('Provide 3 values between 0 and 719.')
value = [0,1,2]
value[0] = input('value 1:')
value[1] = input('value 2:')
value[2] = input('value 3:')
print(value)

laser1 = robotcontrol.get_laser(360)
print(laser1)
