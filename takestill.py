import picamera
import time

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    camera.capture('image.jpg')
    camera.stop_preview()
camera.close()
