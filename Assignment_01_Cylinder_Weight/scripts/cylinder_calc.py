#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from ros_tutorial.msg import Cylinder

from math import pi

radius = 0
radius_squared = 0
height = 0
density = 0 
g = 9.8

radius_found = False
radius_squared_found = False
height_found = False
density_found = False

def radius_callback(data):
    global radius
    global radius_found
    radius = data.data
    radius_found = True

def radius_squared_callback(data):
    global radius_squared
    global radius_squared_found
    radius_squared = data.data
    radius_squared_found = True

def height_callback(data):
    global height
    global height_found
    height = data.data
    height_found = True    

def density_callback(data):
    global density
    global density_found
    density = data.data
    density_found = True  

def calculate():
    if radius_found and radius_squared_found and height_found:
        msg = Cylinder()
        msg.volume = pi * radius_squared * height
        msg.surface_area = 2 * pi * radius * (radius + height)
        msg.weight = msg.volume * density
        pub.publish(msg)

rospy.init_node("cylinder_calc")
rospy.Subscriber("/radius", Float64, radius_callback)
rospy.Subscriber("/radius_squared", Float64, radius_squared_callback)
rospy.Subscriber("/height", Float64, height_callback)
rospy.Subscriber("/density", Float64, density_callback)

pub = rospy.Publisher("/cylinder", Cylinder, queue_size=10)

while not rospy.is_shutdown():
    calculate()
    rospy.sleep(0.1)