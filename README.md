# Project Title

The object of this repository is to create a template that the Junior students can use for developing the code for the Junior Category - Home Robot Challenge 2020

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
You should have install ROS.
You must Install turtlebot repository
You should have create a workspace
```

### Installing

You must install ros_numpy. If you are using other version of ROS, you just have to change to the distribution which you are using.

```
sudo apt-get install ros-kinetic-ros-numpy
```

Then get in the src folder of your workspace
```
cd ~/catkin_ws/src
```
After that clone the repository there
```
https://github.com/huguinsanchez/wrs_challenge.git
```
next step is to compile the new package even thoug you are now using CPP
```
touch ~/catkin_ws/src/wrs_challenge/CMakeLists.txt
cd ~/catkin_ws/
catkin_make
```
End with an example of getting some data out of the system or using it for a little demo

## Running the tests

For create a test of the template working you should launch minimal.launch ans freenect launch on the turtlebot
```
roslaunch turtlebot_bringup minimal.launch
roslaunch freenect_launch freenect.launch
```

### Break down into end to end tests

For see is every thing is working, you should run both codes that are giving by using the launch provided

```
roslaunch wrs_challenge challenge.launch
```

### And coding style tests

Now you just have to look for the comments in the nodes controlToPostion.py and kinect_reader.py for writing the code and make your part. They are located in the scripts folder of the wrs_challenge package

## Authors

* **Victor Hugo Sanchez** - *Initial work* - [PurpleBooth](https://github.com/huguinsanchez)

