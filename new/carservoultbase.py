import RPi.GPIO as GPIO
from time import sleep
import time

in1 = 11
in2 = 12
in3 = 13
in4 = 15
sp = 16
en1 = 21
en = 22
TRIG = 23
ECHO = 24



GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)

GPIO.setup(sp, GPIO.OUT)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.setup(en,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
GPIO.output(TRIG, True)

p=GPIO.PWM(en,1000)
a=GPIO.PWM(en1,1000)
s=GPIO.PWM(sp, 50)

s.start(16)
p.start(22)
a.start(21)

def Setangle(angle):
    duty=((angle/18)+3)
    GPIO.output(sp,True)
    s.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(sp, False)
    s.ChangeDutyCycle(0)


print("\n")
print("Waiting for sensor to Settle")
sleep(2)
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

try:
  while(1):
    Setangle(0)
    x=input()
    print(x)
    p.ChangeDutyCycle(30)
    a.ChangeDutyCycle(30)


    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration*17150
    distance = round(distance, 2)
    print("Distance:",distance,"cm")


    if x=='r':
        a.ChangeDutyCycle(60)
        p.ChangeDutyCycle(60)
        print("turn right")
       # GPIO.output(in1,GPIO.HIGH)
       # GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        sleep(0.5)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        print("stop")

    elif x=='l':
        a.ChangeDutyCycle(60)
        p.ChangeDutyCycle(60)
        print("turn left")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
       # GPIO.output(in3,GPIO.HIGH)
       # GPIO.output(in4,GPIO.LOW)
        sleep(0.5)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        print("stop")

    elif x=='b':
        print("backward")
        a.ChangeDutyCycle(30)
        p.ChangeDutyCycle(30)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        sleep(1)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        print("stop")

    elif x=='f':
        print("forward")
        a.ChangeDutyCycle(30)
        p.ChangeDutyCycle(30)
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        sleep(1)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        print("stop")


    elif x=='e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break

    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
    sleep(2)
    Setangle(135)
    sleep(2)


except KeyboardInterrupt:
    GPIO.cleanup()

