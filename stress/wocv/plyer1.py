import time
from plyer import notification
def notifi1():

    count = 0

    while count < 1:
            count = count + 1
            notification.notify(
                title="Please Wear the Blue Ray Glasses!!",
                message="The blue light glasses are specifically designed to block or filter out the blue light. By wearing blue-light-blocking glasses, people can reduce eye strain, eye damage, and sleep disturbances.",
                timeout=5,app_icon=r"D:\\stress\\wocv\\static\assets\img\\rays.ico")
            
            
            if count == 1:
                return 
def waterremind():

        count = 0


        while count < 1:
            count = count + 1
            notification.notify(
 			title = "Please Drink Water Now!!",
 			message ="Its time for a water break!!",
 			app_icon = "D:\\stress\wocv\static\\assets\\img\\kettle.ico",
 			timeout= 5
 			)
            
            if count == 1:
                return 

