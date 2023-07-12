#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def publish_data():
    rospy.init_node('topic_ornegi', anonymous=True)
    pub = rospy.Publisher('yeni_topic', String, queue_size=10)
    rate = rospy.Rate(1)  # Yayın hızı 10 Hz

    while not rospy.is_shutdown():
        data = "Topic örneği!"
        rospy.loginfo("Yayınlanan veri: %s", data)
        pub.publish(data)
        rate.sleep()

if __name__ == '__main__':
    publish_data()
    



