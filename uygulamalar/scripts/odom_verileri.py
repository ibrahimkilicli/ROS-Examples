#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry

def callback(data):
    # Odom verilerini ekrana yazdırma
    rospy.loginfo("Odom Verileri:")
    rospy.loginfo("Başlık: %s", data.header)
    rospy.loginfo("Child Frame ID: %s", data.child_frame_id)
    rospy.loginfo("Pozisyon - x: %f, y: %f, z: %f", data.pose.pose.position.x, data.pose.pose.position.y, data.pose.pose.position.z)
    rospy.loginfo("Oryantasyon - x: %f, y: %f, z: %f, w: %f", data.pose.pose.orientation.x, data.pose.pose.orientation.y, data.pose.pose.orientation.z, data.pose.pose.orientation.w)
    rospy.loginfo("Hız - lineer: %f, açısal: %f", data.twist.twist.linear.x, data.twist.twist.angular.z)



if __name__ == '__main__':

    rospy.init_node('odom_subscriber', anonymous=True)

    # Odom topic'ine abone olma
    rospy.Subscriber('odom', Odometry, callback)

    # Çalışmayı sürdürme
    rospy.spin()
