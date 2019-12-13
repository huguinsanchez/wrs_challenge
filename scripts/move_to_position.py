#!/usr/bin/env python
import rospy
import math
from geometry_msgs.msg import PoseStamped
from tf.transformations import quaternion_from_euler
from actionlib_msgs.msg import GoalStatusArray

global goal_reached
global pub_simple_goal

goal_reached=0


def callback_base_status(msg):

	global goal_reached
	aux=str(msg.status_list)
	aux= aux.split("\n")
	aux=aux[5].split(" ")
	goal_reached=aux[1]
	#print(goal_reached)


def pub_new_goal(x,y,theta):
	global pub_simple_goal
	global goal_reached
	loop=rospy.Rate(10)
	goal_pose=PoseStamped()
	goal_pose.header.frame_id="map"
	print"new goal"
	goal_pose.header.stamp= rospy.Time.now()
	goal_pose.pose.position.x=x
	goal_pose.pose.position.y=y
	goal_pose.pose.position.z=0.0
	quat=quaternion_from_euler(0, 0, theta)
	goal_pose.pose.orientation.x=quat[0]
	goal_pose.pose.orientation.y=quat[1]
	goal_pose.pose.orientation.z=quat[2]
	goal_pose.pose.orientation.w=quat[3]
	pub_simple_goal.publish(goal_pose)
	loop.sleep()
	goal_reached=0
	rospy.sleep(5.)
	while goal_reached!="3":
		loop.sleep()
	print"end"
	rospy.sleep(2.)


def main():
	global pub_simple_goal
	print "Initializing control to position"
	rospy.init_node('control_to_position', anonymous=True)
	rospy.Subscriber("/move_base/status", GoalStatusArray , callback_base_status)
	pub_simple_goal=rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1)
	loop=rospy.Rate(10)

	rospy.sleep(2.)

	pub_new_goal(0.73,1.49,0.88)
	while not rospy.is_shutdown():
		loop.sleep()



if __name__=='__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass