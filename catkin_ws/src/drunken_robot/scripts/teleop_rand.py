#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist


def twistCallback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.linear.x)


def setup():
     # create node for listening to twist messages
    rospy.init_node("teleop_rand", anonymous=True)

    # subscribe to all
    rospy.Subscriber("cmd_vel", Twist, twistCallback)
    rate = rospy.Rate(100)

    pub = rospy.Publisher("/cmd_vel", Twist)

    # spin() keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == "__main__":
    try:
        setup()
    except rospy.ROSInterruptException:
        print("exit pls")
        pass
