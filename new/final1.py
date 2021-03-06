import RPi.GPIO as GPIO
import time 

out1 = 13
out2 = 11
out3 = 15
out4 = 12

i=0
positive=0
negative=0
y=0
m=0


GPIO.setmode(GPIO.BOARD)
GPIO.setup(out1,GPIO.OUT)
GPIO.setup(out2,GPIO.OUT)
GPIO.setup(out3,GPIO.OUT)
GPIO.setup(out4,GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)



def reference():  #hits the limit switch move forward for 3cm
  print("LS move forward 3cm reference")
  d = 100 #move forward for 100 = 3cm 
  i = 0
  positive = 0
  negative = 0
  e = 0
  for e in range(d,0,-1):
             # var1=GPIO.input(23)
    if negative==1:
        if i==3:
            i=0
        else:
            i=i+1
        y=y+2
        negative=0
    positive=1
    if i==0:
        GPIO.output(out1,GPIO.HIGH)
        GPIO.output(out2,GPIO.HIGH)
        GPIO.output(out3,GPIO.LOW)
        GPIO.output(out4,GPIO.LOW)
        time.sleep(0.01)
                 # i=i+1
    elif i==1:    
        GPIO.output(out1,GPIO.LOW)
        GPIO.output(out2,GPIO.HIGH)
        GPIO.output(out3,GPIO.HIGH)
        GPIO.output(out4,GPIO.LOW)
        time.sleep(0.01)
                 # i=i+1
    elif i==2:
        GPIO.output(out1,GPIO.LOW)
        GPIO.output(out2,GPIO.LOW)
        GPIO.output(out3,GPIO.HIGH)
        GPIO.output(out4,GPIO.HIGH)
        time.sleep(0.01)
                 # i=i+1
    elif i==3:    
        GPIO.output(out1,GPIO.HIGH)
        GPIO.output(out2,GPIO.LOW)
        GPIO.output(out3,GPIO.LOW)
        GPIO.output(out4,GPIO.HIGH)
        time.sleep(0.01)
    if i==3:
        i=0
        continue
             # if var1==True:
    i=i+1


def move(): #move the motor with ls check
    if i==0 and var1==True:
        GPIO.output(out1,GPIO.HIGH)
        GPIO.output(out2,GPIO.HIGH)
        GPIO.output(out3,GPIO.LOW)
        GPIO.output(out4,GPIO.LOW)
        time.sleep(0.01)
       # m=m+1
                 # i=i+1
    elif i==1 and var1==True:    
        GPIO.output(out1,GPIO.LOW)
        GPIO.output(out2,GPIO.HIGH)
        GPIO.output(out3,GPIO.HIGH)
        GPIO.output(out4,GPIO.LOW)
        time.sleep(0.01)
       # m=m+1
                 # i=i+1
    elif i==2 and var1==True:
        GPIO.output(out1,GPIO.LOW)
        GPIO.output(out2,GPIO.LOW)
        GPIO.output(out3,GPIO.HIGH)
        GPIO.output(out4,GPIO.HIGH)
        time.sleep(0.01)
       # m=m+1
                 # i=i+1
    elif i==3 and var1==True:    
        GPIO.output(out1,GPIO.HIGH)
        GPIO.output(out2,GPIO.LOW)
        GPIO.output(out3,GPIO.LOW)
        GPIO.output(out4,GPIO.HIGH)
        time.sleep(0.01)
       # m=m+1
                 # i=i+1
  #  elif var1==False:
   #     GPIO.output(out1,GPIO.HIGH)
    #    GPIO.output(out2,GPIO.HIGH)
     #   GPIO.output(out3,GPIO.HIGH)
      #  GPIO.output(out4,GPIO.HIGH)
       # time.sleep(2)
       # reference()
       # x=0
       # y=0
       # return x, y;


print ("Give some +ve and -ve values in measurement in Cm.....")

try:
   while(1):
      print(m)
      GPIO.output(out1,GPIO.LOW)
      GPIO.output(out2,GPIO.LOW)
      GPIO.output(out3,GPIO.LOW)
      GPIO.output(out4,GPIO.LOW)
      z = input()
      c = int(z)
      x = c*33
      if c>90 and c<=-90:
          print("value should be less than 90cm..")
          print("type in the value")
          getvalue()
          z = input()
          c = int(z)
          x = c*33

      elif x>0 and x<=3000:
          for y in range(x,0,-1):
              var1=GPIO.input(23)
              m=m+1
              if negative==1:
                  if i==3:
                      i=0
                  else:
                      i=i+1
                  y=y+2
                  negative=0
              positive=1
              move()

              if var1==False:
                GPIO.output(out1,GPIO.HIGH)
                GPIO.output(out2,GPIO.HIGH)
                GPIO.output(out3,GPIO.HIGH)
                GPIO.output(out4,GPIO.HIGH)
                time.sleep(2)
                reference()
                break

              if i==3:
                  i=0
                  continue
             # if var1==True:
              i=i+1
             # print(i)
      
      
      elif x<0 and x>=-3000:
          x=x*-1
          for y in range(x,0,-1):
              var1=GPIO.input(23)
              if positive==1:
                  if i==0:
                      i=3
                  else:
                      i=i-1
                  y=y+3
                  positive=0
              negative=1
              move()
                 # i=i-1
              if var1==False:
                GPIO.output(out1,GPIO.HIGH)
                GPIO.output(out2,GPIO.HIGH)
                GPIO.output(out3,GPIO.HIGH)
                GPIO.output(out4,GPIO.HIGH)
                time.sleep(2)
                reference()
                break
                 # i=i-1
              if i==0:
                  i=3
                  continue
             # if var1==True:
              i=i-1 




              
except KeyboardInterrupt:
    GPIO.cleanup()

