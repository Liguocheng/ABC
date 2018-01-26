import time
import os
import RPi.GPIO as GPIO  # new
import cv2
GPIO.setmode(GPIO.BCM)  # new
GPIO.setup(23, GPIO.IN, GPIO.PUD_UP)  # new


    
GPIO.wait_for_edge(23, GPIO.FALLING)

os.system("python3 camera.py")
os.system("python led.py")

    
GPIO.cleanup()
