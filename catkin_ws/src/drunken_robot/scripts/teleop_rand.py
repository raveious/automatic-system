#!/usr/bin/env python

# publisher + subscriber that reads cmd_vel from Jackal and
# either generates a random movement or halts for Jckal to complete
# keyboard teleop movement

# Intro to Robotics - EE5900 - Spring 2017
#          Assignment #2

#       Project #2 Group #2
#         Ian (Team Lead)
#           Haden
#           Akhil
#
# Revision: v1.2

# imports
import rospy
import random
import sys
from geometry_msgs.msg import Twist

last_twist_time_time = 0.0

# define callback for twist
def twistCallback(data):
    global last_twist_time_time
    last_twist_time_time = rospy.get_time()

# define setup and run routine
def setup():
    # get initial parameters
    user_rate  = rospy.get_param("/teleop_rand/drunken_robot/user_rate")

    # create node for listening to twist messages
    rospy.init_node("teleop_rand")

    # subscribe to all
    rospy.Subscriber("cmd_vel", Twist, twistCallback)
    rate = rospy.Rate(user_rate)

    # publish to cmd_vel of the jackal
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

    # loop
    while not rospy.is_shutdown():
        # get delay parameter
        delay = rospy.get_param("/teleop_rand/drunken_robot/delay")

        # check for keyboard teleop
        if last_twist_time_time + delay < rospy.get_time():
            # get parameters
            linear_min  = rospy.get_param("/teleop_rand/drunken_robot/linear_min")
            linear_max  = rospy.get_param("/teleop_rand/drunken_robot/linear_max")
            angular_min = rospy.get_param("/teleop_rand/drunken_robot/angular_min")
            angular_max = rospy.get_param("/teleop_rand/drunken_robot/angular_max")

            # generate random movement mapping
            map = [random.randrange(linear_min,linear_max), random.randrange(angular_min,angular_max)]

            # push Twist msgs
            motion = Twist()
            motion.linear.x = map[0]
            motion.angular.z = map[1]

            # publish Twist
            pub.publish(motion)
            pub = rospy.Publisher("/jackal_velocity_controller/cmd_vel", Twist, queue_size=10)

            # rospy.loginfo('user_rate=%d  linear_min=%d  linear_max=%d  angular_min=%d  angular_max=%d'%(user_rate, linear_min, linear_max, angular_min, angular_max))
            # rospy.loginfo("drunk mode x = {} z = {}".format(motion.linear.x, motion.angular.z))
            rospy.logdebug("drunk mode x = {} z = {}".format(motion.linear.x, motion.angular.z))
        else:
            rospy.logdebug("waiting for input to stop")

        rate.sleep()


# standard ros boilerplate
if __name__ == "__main__":
    try:
        setup()
    except rospy.ROSInterruptException:
        pass
