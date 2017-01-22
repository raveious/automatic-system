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
import sys
from geometry_msgs.msg import Twist

last_twist_time_time = 0.0
delay = 2.0

# Read command line parameters and form key map
# Usage: teleop_rand.py <rate> <linear_min> <linear_max> <angular_min> <angular_max>
def readParameters():
    global user_rate, linear_min, linear_max, angular_min, angular_max

    # default assignments
    user_rate = 2
    linear_min = -1
    linear_max = 2
    angular_min = -1
    angular_max = 2

    # check args
    if len(sys.argv)>1:
        user_rate = int(sys.argv[1])

    if len(sys.argv)>2:
        linear_min = int(sys.argv[2])

    if len(sys.argv)>3:
        linear_max = int(sys.argv[3])

    if len(sys.argv)>4:
        angular_min = int(sys.argv[4])
   
    if len(sys.argv)>5:
        angular_max = int(sys.argv[5])



def twistCallback(data):
    global last_twist_time_time
    last_twist_time_time = rospy.get_time()


def setup():
    readParameters()

     # create node for listening to twist messages
    rospy.init_node("teleop_rand")

    # subscribe to all
    rospy.Subscriber("cmd_vel", Twist, twistCallback)
    rate = rospy.Rate(user_rate)

    pub = rospy.Publisher("/jackal_velocity_controller/cmd_vel", Twist, queue_size=10)

    while not rospy.is_shutdown():

        # check for keyboard teleop
        if last_twist_time_time + delay < rospy.get_time():
            # generate random movement mapping
            map = [random.randrange(linear_min,linear_max), random.randrange(angular_min,angular_max)]
            # map = [random.randrange(-1,2), random.randrange(-1,2)]

            motion = Twist()
            # push Twist msgs
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



if __name__ == "__main__":
    try:
        setup()
    except rospy.ROSInterruptException:
        print("exit pls")
        pass
