#!/usr/bin/env python3
import rospy
import random
from random import random
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import math

my_pi=(1/360)*math.pi*2
aci=0.4
def listener():
	rospy.init_node('listener' , anonymous=False)
	sub=rospy.Subscriber("/scan",LaserScan,cb_scan,queue_size=1)
	rospy.spin()
def cb_scan(data):
	pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
	twist_msg=Twist()
	twist_msg.linear.x=0.1
	pub.publish(twist_msg)
	a=[]
	b=[]
	e=[]
	e=range(0,361)
	c=[]
	c.extend(data.ranges[30:61])
	b.extend(data.ranges[300:331])
	d=[]
	a=data.ranges
	print(a[0],a[90],a[180],a[270])


	min_dizi=data.ranges[0]


	if min_dizi>1:
		twist_msg.angular.z=aci
		twist_msg.linear.x=0.0
		pub.publish(twist_msg)
	elif min_dizi<=1:
		twist_msg.angular.z=0
		twist_msg.linear.x=0.1
		pub.publish(twist_msg)
	else:
		twist_msg.angular.z=0
		twist_msg.linear.x=0.6
		pub.publish(twist_msg)
	
listener()
