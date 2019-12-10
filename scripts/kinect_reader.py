#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose
from sensor_msgs.msg import Image, PointCloud2
import cv2
from cv_bridge import CvBridge
import pcl
import ros_numpy
import numpy as np
global centroid_person
global rgb_mat
global depth_mat
global display

rgb_mat=0
depth_mat=0
display =False
centroid_person=Pose()

def callback_rgb_rect(msg):
	global rgb_mat
	#print "rgb rows: " +str(msg.height)
	#print "rgb columns: "+str(msg.width)
	#print "rgb encoding: "+str(msg.encoding)
	bridge_rgb=CvBridge()
	rgb_mat=bridge_rgb.imgmsg_to_cv2(msg,msg.encoding)

def callback_depth_rect(msg):
	global depth_mat
	global display
	#print "depth rows: "+str(msg.height)
	#print "depth columns: "+str(msg.width)
	#print "depth encoding: "+str(msg.encoding)
	display=True
	bridge_depth=CvBridge()
	depth_mat=bridge_depth.imgmsg_to_cv2(msg,msg.encoding)

def callback_point_clod(msg):
	global centroid_person
	pc = ros_numpy.numpify(msg)

	#pc[j][i] => (x, y, z)
	#i: 0...619 ~ width
	#j: 0...479 ~ height
	#x, positive from the center of the camera to the right
	#y, positive from the center of the camera to the bottom
	#z, positive from the center of the camera to the front

	#Example of read a point in the particle_cloud
	i = 320 
	j = 240 

	print "central point" 
	print pc[j][i]

	#Find the centroid of the closest object
	#Insert your code here



def main():
	global centroid_person
	global rgb_mat
	global depth_mat
	global display

	print "Initializing kinect_reader"
	rospy.init_node('kinect_reader', anonymous=True)
	rospy.Subscriber("/camera/rgb/image_rect_color", Image , callback_rgb_rect)
	rospy.Subscriber("/camera/depth_registered/image", Image, callback_depth_rect)
	rospy.Subscriber("/camera/depth_registered/points", PointCloud2, callback_point_clod)
	pub_centroid=rospy.Publisher('/centroid_person', Pose, queue_size=1)
	loop=rospy.Rate(10)

	centroid_person.position.x=0
	centroid_person.position.y=0
	centroid_person.position.z=0
	centroid_person.orientation.x=0
	centroid_person.orientation.y=0
	centroid_person.orientation.z=0
	centroid_person.orientation.w=0

	while not rospy.is_shutdown():
		#print display
		if(display):
			cv2.imshow("rgb", rgb_mat)
			cv2.imshow("depth", depth_mat)
			cv2.waitKey(1)
		
		pub_centroid.publish(centroid_person)
		loop.sleep()



if __name__=='__main__':
	try:
		main()
		cv2.destroyAllWindows()
	except rospy.ROSInterruptException:
		pass