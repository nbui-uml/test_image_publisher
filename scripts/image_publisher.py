#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image as ImageMsg
from PIL import Image
import numpy as np

rospy.init_node("image_publisher")
pub = rospy.Publisher("spot/camera/frontright/image", ImageMsg, queue_size=10)
pub2 = rospy.Publisher("spot/camera/frontleft/image", ImageMsg, queue_size=10)
img = Image.open("/home/csrobot/catkin_ws/src/test_image_publisher/resource/amongus.jpg")
img = img.convert("RGB")
img = img.rotate(90)
img2 = Image.open("/home/csrobot/catkin_ws/src/test_image_publisher/resource/lechonk.jpg")
img2 = img2.convert("L")
img2 = img2.rotate(90)

msg = ImageMsg()
msg.height = img.height
msg.width = img.width
msg.encoding = "rgb8"
msg.is_bigendian = False
msg.step = 3*img.width
msg.data = np.array(img).tobytes()

msg2 = ImageMsg()
msg2.height = img2.height
msg2.width = img2.width
msg2.encoding = "mono8"
msg2.is_bigendian = False
msg2.step = img2.width
msg2.data = np.array(img2).tobytes()

print("Publishing...")
rate = rospy.Rate(2)
while not rospy.is_shutdown():
    msg.header.stamp = rospy.Time.now()
    msg2.header.stamp = rospy.Time.now()
    pub.publish(msg)
    pub2.publish(msg2)
    rate.sleep()