#   Author: Sanal Kumar
#   e-mail: sanaltsk@gmail.com
#   Submission for GSOC2012 Project : SimpleCV
#
#
#   This program is a sample program that shows its utility for helping the blind to help in navigating or cross roads. This is a simple demonstration,
#   this need not work in practical scenarios
#   This program uses a base image which is idle situtation where a user can cross the road consided as "base_image"
#   The new image can be captured with the hand held camera or a mounted camera on the user which consistently captures the road ahead considered as "new_image"


from SimpleCV import *


#
#   check_diff function checks the passed parameter diff_mean is zero or not
#   if  zeros that means the base_image and new _image is similar and there is no deviation from base_image and the user is ready to cross
#   else the base_image and new _image is dis-similar and there is deviation from base_image and the user have to wait till the road clears
#
def check_diff(diff_mean):
    if(diff_mean==(0.0,0.0,0.0)):
        print "Ready To Cross"
    else:
        print "Wait"


#   loading two images zebra_crossing and zebra_crossing_with_car
#
#   zebra_crossing is considered as the base image with no traffic
#
#   zebra_crossing_with car is considered as the image which deviates from the base image
#
#

zebra_crossing=Image("zebra_crossing.jpg")
zebra_crossing_with_car=Image("zebra_crossing_with_car.jpg")

base_image = zebra_crossing                 # base_image is defined as the zebra_crossing image
new_image = zebra_crossing_with_car         # new_image is defined as the zebra_crossing_with_car image
diff = new_image - base_image               # Calculating the difference between the two images
diff_mean = diff.meanColor()                # Calculating the mean of the difference image

#
#   if the diff_mean returns (0.0,0.0,0.0) the new image is same as base image
#   but if the diff_mean is anything other than (0.0,0.0,0.0) then there is some deviation from the base case
#


#   Scenario 1: when the road is busy
#   calling check_diff with parameter(diff_mean)
print 'Scenario 1:',
check_diff(diff_mean)


new_image2 = base_image                     # New_image2 captures the clear road similar to base_image
diff_new = new_image2 - base_image          # Calculating the difference between the two images new_image2 and base_image
new_diff_mean = diff_new.meanColor()



#   Scenario 2: when the road is cleared off traffic
#   calling check_diff with parameter(new_diff_mean)
print 'Scenario 2:',
check_diff(new_diff_mean)



#####               END_PROGRAM                 #####
