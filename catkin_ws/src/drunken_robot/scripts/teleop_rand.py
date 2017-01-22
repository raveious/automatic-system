#!/usr/bin/env python

# Talker that reads current location temperature and  
# publishes std_msgs to the 'chatter' topic as Float32

# Intro to Robotics - EE5900 - Spring 2017
#          Assignment #2

#       Project #2 Group #2
#         Ian (Team Lead)
#           Haden
#           Akhil
#
# Revision: v1.1

# imports
import rospy
import random
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

    pub = rospy.Publisher("/jackal_velocity_controller/cmd_vel", Twist, queue_size=10)

    while not rospy.is_shutdown():
        # check for keyboard teleop
        if last_twist_time_time + delay < rospy.get_time():
            rospy.loginfo("drunk mode")

            # generate random movement mapping
            map = [random.randrange(-1,2), random.randrange(-1,2)]

            motion = Twist()
            # push Twist msgs
            motion.linear.x = map[0]
            motion.angular.z = map[1]
            
            # publish Twist
            pub.publish(motion)
            pub = rospy.Publisher("/jackal_velocity_controller/cmd_vel", Twist, queue_size=10)

        else:
            rospy.loginfo("waiting for input to stop")

        rate.sleep()



if __name__ == "__main__":
    try:
        setup()
    except rospy.ROSInterruptException:
        print("exit pls")
        pass
