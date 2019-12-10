#!/usr/bin/env python
import rospy
import math
from geometry_msgs.msg import Pose, Twist
from tf.transformations import quaternion_from_euler

global goal_pose
global pub_twist

goal_pose=Pose()
pub_twist=0

def calculate_vel(distance, angle):
	global pub_twist
	speed=Twist()
	loop=rospy.Rate(10)

	print "angle: "+str(angle)
	print "distance: "+str(distance)
	#CHANGE THIS CONSTANTS TO YOUR PROPOUSE
	linear_vel_k=.1
	anglular_vel_k=.1

	if(distance==0 and angle==0):
		speed.linear.x=0
		speed.linear.y=0
		speed.linear.z=0
		speed.angular.x=0
		speed.angular.y=0
		speed.angular.z=0
	else:
		#Set dis variable to your propuse

		speed.linear.x=linear_vel_k*distance
		speed.linear.y=0
		speed.linear.z=0
		speed.angular.x=0
		speed.angular.y=0
		speed.angular.z=-anglular_vel_k*(angle/10)

	pub_twist.publish(speed)
	loop.sleep()


def callback_goal_pose(msg):
	#global goal_pose
	centroid_person=msg

	##set the parameters to functional values for your application
	distance_th=.5  
	angle_th=.50

	#calculate distance and angle from the current pose to the goal pose
	distance=0 #distance of the robot wrt the person should be in meter
	angle=0 #orientation of the robot wrt the person should be in degrees


	#DO NOT FORGET TO CHANGE THE CONSTANTS IN calculate_vel FUNCTION
	if abs(distance)>distance_th and abs(angle)>angle_th:
		calculate_vel(distance,angle)
	elif abs(distance)>distance_th:
		calculate_vel(distance,0)
	elif abs(angle)>angle_th: 
		calculate_vel(0,angle)
	else:
		calculate_vel(0,0)







def main():
	global pub_twist
	print "Initializing control to position"
	rospy.init_node('control_to_position', anonymous=True)
	rospy.Subscriber("/centroid_person", Pose , callback_goal_pose)
	pub_twist=rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=1)
	loop=rospy.Rate(10)


	while not rospy.is_shutdown():
		
		loop.sleep()



if __name__=='__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass