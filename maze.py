import time
from robot_control_class import RobotControl 
robotcontrol = RobotControl() 

class Robo:

    def __init__(self):
        print("intializing...")
        self.laser1 = robotcontrol.get_laser(360)
        self.robotmove_speed = 5
        self.robotmove_time = 1
        self.robotturn_clockwise = "clockwise"
        self.robotturn_speed = 0.8
        self.robotturn_time = 1

    def robotmove(self):
        while self.laser1 > 1:
            robotcontrol.move_straight()
            self.laser1 = robotcontrol.get_laser(360)
            print("distance: ", self.laser1)

        robotcontrol.stop_robot()
        print("I'm too close to the wall...")

    def robotturn(self):
        distance_right = robotcontrol.get_laser(180)
        distance_left = robotcontrol.get_laser(540)
        print("right",distance_right, "left", distance_left)
        if distance_right > distance_left:
            while self.laser1 < 1:
                robotcontrol.turn(self.robotturn_clockwise, self.robotturn_speed, self.robotturn_time)
                self.laser1 = robotcontrol.get_laser(360)
                print("right: distance: ", self.laser1)
        else:
            while self.laser1 < 1:
                robotcontrol.turn("aclockwise", self.robotturn_speed, self.robotturn_time)
                self.laser1 = robotcontrol.get_laser(360)
                print("left: distance: ", self.laser1)

        robotcontrol.stop_robot()
        print("I'll be right back...")

if __name__ == '__main__':

    robo = Robo()

    while not robotcontrol.ctrl_c_f:

        robo.robotmove()
        robo.robotturn()
