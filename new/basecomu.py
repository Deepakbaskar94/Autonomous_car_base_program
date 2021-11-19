import RPi.GPIO as GPIO
from time import sleep
import time
import ova
from device_data import get_device
from luma.core.render import canvas
import os
#os.system('python3 ova.py')

in1 = 11
in2 = 12
in3 = 13
in4 = 15
#sp = 16
en1 = 21
en = 22
TRIGM = 23
ECHOM = 24
TRIGL = 31
ECHOL = 32
TRIGR = 29
ECHOR = 26
i=0
x=0




GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)

#GPIO.setup(sp, GPIO.OUT)
GPIO.setup(TRIGM, GPIO.OUT)
GPIO.setup(ECHOM, GPIO.IN)
GPIO.setup(TRIGL, GPIO.OUT)
GPIO.setup(ECHOL, GPIO.IN)
GPIO.setup(TRIGR, GPIO.OUT)
GPIO.setup(ECHOR, GPIO.IN)



GPIO.setup(en,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

GPIO.output(TRIGM, True)
GPIO.output(TRIGL, True)
GPIO.output(TRIGR, True)



p=GPIO.PWM(en,1000)
a=GPIO.PWM(en1,1000)
#s=GPIO.PWM(sp, 50)

#s.start(16)
p.start(22)
a.start(21)

'''def Setangle(angle):
    duty=((angle/18)+3)
    GPIO.output(sp,True)
    s.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(sp, False)
    s.ChangeDutyCycle(0)'''

def ult():
    GPIO.output(TRIGM, True)
    time.sleep(0.00001)
    GPIO.output(TRIGM, False)

    while GPIO.input(ECHOM)==0:
        pulse_start = time.time()

    while GPIO.input(ECHOM)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    global distance
    distance = pulse_duration*17150
    distance = round(distance, 2)
    print("Distance:",distance,"cm")
    global displaydata
    displaydata = str(distance)
    #main()
###############################################    
    GPIO.output(TRIGL, True)
    time.sleep(0.00001)
    GPIO.output(TRIGL, False)

    while GPIO.input(ECHOL)==0:
        pulse_start = time.time()

    while GPIO.input(ECHOL)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    global distance1
    distance1 = pulse_duration*17150
    distance1 = round(distance1, 2)
    print("DistanceL:",distance1,"cm")
    global displaydata1
    displaydata1 = str(distance1)
#############################################
    GPIO.output(TRIGR, True)
    time.sleep(0.00001)
    GPIO.output(TRIGR, False)

    while GPIO.input(ECHOR)==0:
        pulse_start = time.time()

    while GPIO.input(ECHOR)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    global distance2
    distance2 = pulse_duration*17150
    distance2 = round(distance2, 2)
    print("DistanceR:",distance2,"cm")
    global displaydata2
    displaydata2 = str(distance2)



def stop():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

def main():
    #device = get_device()
    with canvas(device) as draw:
        top = 6
        #size = draw.textsize('World!')
        draw.text((device.width - 80, top), displaydata, fill = "cyan")
        draw.rectangle(device.bounding_box, outline = "White")
        

print("\n")
print("Waiting for sensor to Settle")
sleep(2)  
device = get_device()
try:
  while(1):
    p.ChangeDutyCycle(30)
    a.ChangeDutyCycle(30)
    ult()
    ova.oled_data(displaydata, displaydata1, displaydata2)
    #os.system('python3 ova.py') 
    #Setangle(95)
    ult()
    #main()
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    if distance<45 or distance1<45 or distance2<45:
        stop()
        sleep(1)
        ult()
        c=distance
        print("c distance is", c)
        #Setangle(135)
        ult()
        l=distance
        print("l distance is ",l)
        #Setangle(25)
        ult()
        r=distance
        print("r distance is ",r)
        if (r>l) and (r>c):
            largest = r
            print("the longest distance is r and length ",r)
            print("Rotate Right side Wheel")
            p.ChangeDutyCycle(30)
            a.ChangeDutyCycle(30)
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.HIGH)
            sleep(1)
            stop()
            sleep(1)
            p.ChangeDutyCycle(70)
            #GPIO.output(in1,GPIO.HIGH)
            #GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.HIGH)
            sleep(1)
            stop()

        elif (l>r) and (l>c):
            largest = l
            print("the longest distance is l and length ",l)
            print("Rotate Left side wheel")
            p.ChangeDutyCycle(30)
            a.ChangeDutyCycle(30)
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.HIGH)
            sleep(1)
            stop()
            sleep(1)
            a.ChangeDutyCycle(70)
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            sleep(1)
            stop()

        else:
            largest = c
            print("the longest distance is c and length ",c)


except KeyboardInterrupt:
    GPIO.cleanup()

