#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
import math
from geometry_msgs.msg import Twist
import time 
import tf

# Global değişkenler
x_robot = 0
y_robot = 0
yaw = 0
x_goal = 2
y_goal = 0
min_value_right = 0
min_value_front = 0
min_value_left = 0 
is_stop_moving = False 
vel_msg = Twist()

# Lazer tarama verileri için geri çağırma fonksiyonu.
def scan_callback(scan_data):
    global min_value_right, min_value_front, min_value_left
    ranges = scan_data.ranges
    front_range = ranges[345:359] + ranges[0:15]
    right_range = ranges[80:100]
    left_range = ranges[260:280]
    min_value_left = min(left_range)
    min_value_right = min(right_range)
    min_value_front = min(front_range)

# Duruş verileri için geri çağırma fonksiyonu.
def pose_callback(pose_data):
    global x_robot, y_robot, yaw
    
    x_robot = pose_data.pose.pose.position.x
    y_robot = pose_data.pose.pose.position.y

    quaternion = (
        pose_data.pose.pose.orientation.x,
        pose_data.pose.pose.orientation.y,
        pose_data.pose.pose.orientation.z,
        pose_data.pose.pose.orientation.w)
    rpy = tf.transformations.euler_from_quaternion(quaternion)
    yaw = rpy[2]

# Robotu hedefe doğru döndürmek için fonksiyon.
def rotate_to_goal_state(): 
    print(">>>>> Hedefe doğru dön")
    global x_goal, y_goal, yaw, vel_msg
    desired_angle_goal = math.atan2(y_goal - y_robot, x_goal - x_robot)
    K_angular = 0.5
    angular_speed = (desired_angle_goal - yaw) * K_angular

    # Robot hedefe doğru dönene kadar devam et.
    while True:
        vel_msg.angular.z = angular_speed
        velocity_publisher.publish(vel_msg)
        if desired_angle_goal < 0:
            if (desired_angle_goal - yaw) > -0.1:
                break
        else:
            if (desired_angle_goal - yaw) < 0.1:
                break

    # Dönmeyi durdur.
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)    

# Robotu ileri hareket ettirmek için fonksiyon.
def move_forward_state():
    print(">>>>> İleri hareket et")
    vel_msg = Twist()
    vel_msg.linear.x = 0.2
    velocity_publisher.publish(vel_msg)
    return

# Duvarı takip etme durumuna geçmek için fonksiyon.
def follow_wall_state():
    if min_value_right > min_value_left:
        angle = get_wall_angle(True) 
        print(">>>>> Açıyı sağa (90 derece) değiştir: ", angle)               
    else: 
        angle = get_wall_angle(False) 
        print(">>>>> Açıyı sola (90 derece) değiştir: ", angle)                 
    if (angle - yaw) < 0:                 
        while (angle - yaw) < -0.1:    
            vel_msg.angular.z = (angle - yaw) * 0.9
            velocity_publisher.publish(vel_msg)
    else: 
        while (angle - yaw) > 0.1:    
            vel_msg.angular.z = (angle - yaw) * 0.9
            velocity_publisher.publish(vel_msg)
    vel_msg.angular.z = 0

    # Her döndürme sonrası robotu bir süreliğine ileri hareket ettir.
    if min_value_front > 0.5:
        time = 0
        t0 = rospy.Time.now().to_sec()
        while time < 2.5 and min_value_front > 0.5:
            t1 = rospy.Time.now().to_sec()
            time = t1 - t0
            vel_msg.linear.x = 0.2
            velocity_publisher.publish(vel_msg)

# Hedefe ulaşıldığını kontrol etmek için fonksiyon.
def is_goal_reached(): 
    if (x_goal - 0.05 < x_robot < x_goal + 0.05) and (y_goal - 0.05 < y_robot < y_goal + 0.05):  
        return True 
    return False

# Robotun hedefe doğru yönlendirildiğini kontrol etmek için fonksiyon.
def is_towards_goal(): 
    desired_angle_goal = math.atan2(y_goal - y_robot, x_goal - x_robot)
    if abs(desired_angle_goal - yaw) < 0.4:
        return True
    return False 

# Duvarın açısını almak için fonksiyon.
def get_wall_angle(is_right): 
    angle = 0 
    if ((min_value_left > 0.6 and yaw > 0) or (min_value_right > 0.6 and yaw < 0)) and not ((0.0 < yaw < 0.002) or (-3.16< yaw <-3.0)):
        angle = 0.0 if is_right else -math.pi/2
    else: 
        angle = -math.pi/2 if is_right else math.pi/2
    return angle     

# Programın ana kısmı.
if __name__ == '__main__':
    # ROS düğümlerini ayarla.
    rospy.init_node('scan_node', anonymous=True)
    rospy.Subscriber("/scan", LaserScan, scan_callback)
    rospy.Subscriber("/odom", Odometry, pose_callback)
    cmd_vel_topic = "/cmd_vel"
    velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)
    time.sleep(2.0)

    while True:
        # Veriyi yazdır.
        print(">>>>> Veri")
        print("min_value_right: " + str(min_value_right))
        print("min_value_left: " + str(min_value_left))
        print("min_value_front: " + str(min_value_front))
        print("yaw: " + str(yaw))

        if min_value_front > 0.4:
            # Eğer robot duvarı takip etmiyorsa...
            if not ((min_value_right < 0.4 and yaw < 0) or (min_value_left < 0.4 and yaw > 0)):  
                rotate_to_goal_state()
                is_stop_moving = False 
            while min_value_front > 0.4:
                move_forward_state()

                # Eğer robot duvarı takip etmiyorsa...
                if not ((min_value_right < 0.4 and yaw < 0) or (min_value_left < 0.4 and yaw > 0)):
                    # Eğer robot hedefe doğru yönlendirilmediyse...
                    if (not is_towards_goal()) and not is_stop_moving: 
                        print(">>>>> İleri hareketi durdur")
                        vel_msg.angular.z = 0.0
                        vel_msg.linear.x = 0.0
                        velocity_publisher.publish(vel_msg)
                        is_stop_moving = True 
                        break
                            
        else:
            follow_wall_state()

        # Temizlik yap.
        vel_msg.angular.z = 0.0
        vel_msg.linear.x = 0.0
        velocity_publisher.publish(vel_msg)
        
        print(">>>>> İterasyon Tamamlandı")
        

        # Hedefe ulaşıldı mı diye kontrol et.
        is_reached = is_goal_reached()
        if is_reached == True:
            print(">>>>> Hedefe ulaşıldı")
            break                                            







