#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


class TurtlebotController:
    def __init__(self):
        rospy.init_node('turtlebot_controller')
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber('/scan', LaserScan, self.scan_callback)
        self.rate = rospy.Rate(5)
        self.obstacle_detected = False

    def scan_callback(self, data):
        ranges = data.ranges
        front_ranges = ranges[0:15] + ranges[345:359]  

        if min(front_ranges) < 1.0:  
            self.obstacle_detected = True
        else:
            self.obstacle_detected = False

    def turn_left(self):
        self.stop()
        rospy.sleep(1)  
        twist = Twist()
        twist.angular.z = 1.570796327 # 90 derece dönüş 
        self.pub.publish(twist)
        rospy.sleep(0.84)  

    def stop(self):
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        self.pub.publish(twist)

    def run(self):
        while not rospy.is_shutdown():
            if self.obstacle_detected:
                self.turn_left()
            else:
                twist = Twist()
                twist.linear.x = 0.2  
                twist.angular.z = 0.0
                self.pub.publish(twist)

            self.rate.sleep()

if __name__ == '__main__':
    controller = TurtlebotController()
    controller.run()