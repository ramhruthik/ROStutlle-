import time
from robot_control_class import RobotControl
robotcontrol = RobotControl() 


def robotmove(a,b,c):
    result = robotcontrol.move_straight_time(a,b,c)
    print(result)

def robotturn(a,b,c):
    result = robotcontrol.turn(a,b,c)
    print(result)
end = "no"
while end != "yeah":
    a = raw_input('direction: forward or backward')
    b = input('speed: m/s ')
    c = input('time: mon')
    robotmove(a,b,c)
    print('turn function')
    d = raw_input('clockwise: ')
    b = input('speed: m/s ')
    c = input('time: mon ')
    robotturn(d,b,c)
    fim = raw_input("final")
