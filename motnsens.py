import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.IN)
while True:
    i=GPIO.input(37)
    if i==0:
        print "No intruders",i
        time.sleep(0.5)
    elif i==1:
        print "intruder detected",i
        time.sleep(0.5)
