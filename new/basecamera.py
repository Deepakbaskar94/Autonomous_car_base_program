from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180
'''camera.start_preview()
sleep(5)
camera.capture('/home/pi/image.jpg')
camera.stop_preview()'''

camera.start_preview()
camera.start_recording('/home/pi/video.h264')
sleep(20)
camera.stop_recording()
camera.stop_preview()
