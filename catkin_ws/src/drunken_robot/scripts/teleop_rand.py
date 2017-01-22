#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

last_twist_time_time = 0.0
delay = 2.0


def twistCallback(data):
    global last_twist_time_time

    last_twist_time_time = rospy.get_time()
    rospy.loginfo("Received twist message")


def setup():
     # create node for listening to twist messages
    rospy.init_node("teleop_rand", anonymous=True)

    # subscribe to all
    rospy.Subscriber("cmd_vel", Twist, twistCallback)
    rate = rospy.Rate(5)

    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

    while not rospy.is_shutdown():
        if last_twist_time_time + delay < rospy.get_time():
            rospy.loginfo("drunk mode")
        else:
            rospy.loginfo("waiting for input to stop")
        rate.sleep()



if __name__ == "__main__":
    try:
        setup()
    except rospy.ROSInterruptException:
        print("exit pls")
        pass
