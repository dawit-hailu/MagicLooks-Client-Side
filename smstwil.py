import json
import time
import twilio
import dropbox
import picamera
import requests
import datetime
import twilio.rest
import RPi.GPIO as GPIO
from twilio.rest import TwilioRestClient


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.IN)
account_sid = "AC33e44f399e3d2d7bfa188651de49f3f1"
auth_token = "bce1bbb2a6114d7a21ae44613cc3281c"



    
while True:
    i=GPIO.input(37)

    if i==0:
        time.sleep(0.5)

    elif i==1:
        print "intruder detected",i
        camera = picamera.PiCamera()
        camera.capture('image.jpg')
        camera.close()

#suffix = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        filename = "image.jpg"
 
        client = dropbox.client.DropboxClient('sbC58yZoOMAAAAAAAAAANeU0Kz1SCdJSlFfgMmfRXuLitRxSxAWa1ft8QyjgliJh')
        f = open('/home/pi/Desktop/image.jpg', 'rb')
        response = client.put_file(filename, f)
        print "uploaded:", response

        strResponse = str(response)
        fileName= strResponse.split(",")[8].split("/")[1].rstrip("'").split(" ")

        mesg = "Intruder detected! https://www.dropbox.com/home/Apps/miflect?preview="+fileName[0]+"+"+fileName[1] 
        client = TwilioRestClient(account_sid, auth_token)
        message = client.messages.create(to="+15109657717", from_="+14088729293",
                                     body = mesg)
        time.sleep(5)
