# Task 3
#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(23, GPIO.OUT)
#GPIO.output(23, GPIO.HIGH)

import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.output(23, GPIO.HIGH)
sleep(1)
GPIO.cleanup()
