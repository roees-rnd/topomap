#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseWithCovarianceStamped



def callback(data):
    nav = Odometry
    import pdb;pdb.set_trace()
#    nav.header.stamp = data.header.stamp
#    nav.pose = data.pose
#    nav.twist.twist.linear.x=0
#    nav.twist.twist.linear.y=0
#    nav.twist.twist.linear.z=0
#    nav.twist.twist.angular.x=0
#    nav.twist.twist.angular.y=0
#    nav.twist.twist.angular.z=0


    #print(nav.pose)
    pub.publish(nav)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=False)

    rospy.Subscriber("poseupdate", PoseWithCovarianceStamped, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


#pub = rospy.Publisher('odom', Odometry,queue_size=10)

if __name__ == '__main__':
    pub = rospy.Publisher('odom', Odometry, queue_size=0)
    listener()

