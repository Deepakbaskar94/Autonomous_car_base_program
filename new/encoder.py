import RPi.GPIO as GPIO
from time import sleep

var1 = 1
var2 = 0
en1 = 21
i = 0

in1 = 11
in2 = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(en1, GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

a=GPIO.PWM(en1,1000)

a.start(21)
i = 1
while i < 10:
        print(i)
        a.ChangeDutyCycle(90)
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        var1 = GPIO.input(23)
        if var1==0:
            i=i+1
            print("inside condition")
            print(i)
        else:
            print(var1)
        print(var1)
        sleep(0.01)

print("Completed the cycle")
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

#except KeyboardInterrupt:
 #   GPIO.output(in1,GPIO.LOW)
  #  GPIO.output(in2,GPIO.LOW)
