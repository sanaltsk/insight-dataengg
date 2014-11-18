#   Author: Sanal Kumar
#   e-mail: sanaltsk@gmail.com
#   Submission for GSOC2012 Project : SimpleCV
#
#
#   This program is a sample program that shows its utility for detecting intrusion 
#   through a door. The head of the door consists of CCTV which constantly feeds
#   the program with images. Any change from normal behaviour is considered as
#   an intrusion and alarm is raised.
#
#

from SimpleCV import *


#
#   check_diff function checks the passed parameter diff_mean is zero or not
#   if  base_image and new _image is dis-similar and there is deviation from base_image and
#   then alarm is raised
#
def check_diff(base_image,new_image,i):
    diff = new_image - base_image               # Calculating the difference between the two images
    diff_mean = diff.meanColor()  
    if(diff_mean!=(0.0,0.0,0.0)):
        print "Trigger Alarm --Intrusion detected in "+str(i)+" Frame"


#
#   Actually the footage has to taken from a camera, using the below code
#   cam=Camera()
#   while(1):
#      new_image=cam.getImage()
#      check_diff(base_image,new_image)
#       
#   For the sake of demonstration I would be having a series of CCTV Images
#   opened and do the computation
#
#
#

base_footage=Image("base_footage.jpg")  #Base Image is initialized, this is the ideal behaviour
i=1                                     #any change in Base image will trigger alarm
while(i<7):
    new_footage=Image("CC_TV_Footage_"+str(i)+".jpg")
    check_diff(base_footage,new_footage,i)  # Checking difference between base footage and new footage
    i=i+1
#####               END_PROGRAM                 #####
