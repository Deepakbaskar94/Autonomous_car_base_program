import RPi.GPIO as GPIO
from time import sleep

in1 = 11
in2 = 12
in3 = 13
in4 = 15
en = 22
en1 = 21
i = 0
c = 50
var1 = 1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)

GPIO.setup(en,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)
#GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

p=GPIO.PWM(en,1000)
a=GPIO.PWM(en1,1000)

p.start(22)
a.start(21)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

try:
  while(1):

    x=input()
    print(x)
    p.ChangeDutyCycle(30)
    a.ChangeDutyCycle(30)
    if x=='r':
       # a.ChangeDutyCycle(40)
       # p.ChangeDutyCycle(100)
        print("turn right")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
       # GPIO.output(in3,GPIO.LOW)
       # GPIO.output(in4,GPIO.HIGH)
        sleep(1)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        print("stop")

    elif x=='l':
       # a.ChangeDutyCycle(100)
       # p.ChangeDutyCycle(40)
        print("turn left")
       # GPIO.output(in1,GPIO.LOW)
       # GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        sleep(1)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        print("stop")

    elif x=='b':
    # while i < c:
        print("backward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
       # if var1==0:
        #    i=i+1
         #   print("inside condition")
          #  print(i)
       # else:
        #    print(var1)
       # sleep(0.01)
    # i=0  
        sleep(2)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        print("stop")

    elif x=='f':
   #  while i < c:
        print("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
     #   var1 = GPIO.input(23)
       # if var1==0:
        #    i=i+1
         #   print("inside condition")
          #  print(i)
       # else:
        #    print(var1)
       # sleep(0.01)
    # i=0   
        sleep(2)
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

except KeyboardInterrupt:
    GPIO.cleanup()

