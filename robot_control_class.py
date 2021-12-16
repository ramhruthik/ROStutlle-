from geometry_msgs.msg import Twist
import rospy as rp

import time
from sensor_msgs.msg import LaserScan 


class RobotControl():

    def __init__(self):
        rp.init_node('robot_control_node', anonymous=True)
        self.vel_publisher_v = rp.Publisher('/cmd_vel', Twist, queue_size=1)
        self.laser_subscriber_v = rp.Subscriber(
            '/kobuki/laser/scan', LaserScan, self.laser_callback)
        self.commands = Twist()
        self.laser_msgs = LaserScan()
        self.ctrl_c_f = False
        self.rate_val = rp.Rate(1)
        rp.on_shutdown(self.shutdownhook)

    def publish_once_in_cmd_vel(self):
        while not self.ctrl_c_f :
            connections_num = self.vel_publisher_v.get_num_connections()
            if connections_num > 0:
                self.vel_publisher_v.publish(self.commands)

                break
            else:
                self.rate_val.sleep()

    def shutdownhook(self):
        # works better than the rospy.is_shutdown()
        self.ctrl_c_f  = True

    def laser_callback(self, msg):
        self.laser_msgs = msg

    def get_laser(self, pos):
        time.sleep(1)
        return self.laser_msgs.ranges[pos]

    def get_front_laser(self):
        time.sleep(1)
        return self.laser_msgs.ranges[360]

    def get_laser_full(self):
        time.sleep(1)
        return self.laser_msgs.ranges

    def stop_robot(self):

        self.commands.linear.x = 0.0
        self.commands.angular.z = 0.0
        self.publish_once_in_cmd_vel()

    def move_straight(self):

        # Initilize velocities
        self.commands.linear.x = 0.5
        self.commands.linear.y = 0
        self.commands.linear.z = 0
        self.commands.angular.x = 0
        self.commands.angular.y = 0
        self.commands.angular.z = 0

        # Publish the velocity
        self.publish_once_in_cmd_vel()

    def mov_straight_time_val(self, motion, speed, time):

        self.commands.linear.y = 0
        self.commands.linear.z = 0
        self.commands.angular.x = 0
        self.commands.angular.y = 0
        self.commands.angular.z = 0

        if motion == "forward":
            self.commands.linear.x = speed
        elif motion == "backward":
            self.commands.linear.x = - speed

        loop = 0

        while (loop <= time):


            self.vel_publisher_v.publish(self.commands)
            loop += 1
            self.rate_val.sleep()
        motion1=motion

        self.stop_robot()

        s = "Moved robot " + motion1 + " for " + str(time) + "  seconds"
        return s


    def turn(self, clockwise, speed, time):

        # Initilize velocities
        self.commands.linear.x = 0
        self.commands.linear.y = 0
        self.commands.linear.z = 0
        self.commands.angular.x = 0
        self.commands.angular.y = 0


        if clockwise == "clockwise":
            self.commands.angular.z = -speed
        else:
            self.commands.angular.z = speed

        loop = 0

        while (loop <= time):


            self.vel_publisher_v.publish(self.commands)
            loop += 1
            self.rate_val.sleep()


        self.stop_robot()
        clk=clockwise
        s = "Turned robot " + clk + " for " + str(time) + "  seconds"
        return s


if __name__ == '__main__':

    robotcontrol_object_new = RobotControl()
    try:
        robotcontrol_object_new.move_straight()

    except rp.ROSInterruptException:
        pass
