import RPi.GPIO as GPIO
from time import sleep

sp = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sp, GPIO.OUT)

p = GPIO.PWM(sp, 50) # GPIO 17 for PWM with 50Hz
p.start(0) # Initialization


def SetAngle(angle):
    duty =((angle / 18) + 3)
    GPIO.output(sp, True)
    p.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(sp, False)
    p.ChangeDutyCycle(0)

try:
    while True:
        SetAngle(0) 
        sleep(1)
        SetAngle(45) 
        sleep(1)
        SetAngle(90) 
        sleep(1)
        SetAngle(135) 
        sleep(1)
        SetAngle(170)
        sleep(1)

except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
