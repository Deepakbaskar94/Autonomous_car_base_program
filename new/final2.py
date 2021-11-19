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
k=855


GPIO.setmode(GPIO.BOARD)
GPIO.setup(out1,GPIO.OUT)
GPIO.setup(out2,GPIO.OUT)
GPIO.setup(out3,GPIO.OUT)
GPIO.setup(out4,GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)


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
    i=i+1


def move(): #move the motor with ls check
   # if i==0:
    if i==0 and var3==True:
        GPIO.output(out1,GPIO.HIGH)
        GPIO.output(out2,GPIO.LOW)
        GPIO.output(out3,GPIO.LOW)
        GPIO.output(out4,GPIO.LOW)
        time.sleep(0.01)
    elif i==1 and var3==True:
        GPIO.output(out1,GPIO.HIGH)
        GPIO.output(out2,GPIO.HIGH)
        GPIO.output(out3,GPIO.LOW)
        GPIO.output(out4,GPIO.LOW)
        time.sleep(0.01)
    elif i==2 and var3==True:    
        GPIO.output(out1,GPIO.LOW)
        GPIO.output(out2,GPIO.HIGH)
        GPIO.output(out3,GPIO.LOW)
        GPIO.output(out4,GPIO.LOW)
        time.sleep(0.01)
    elif i==3 and var3==True:
        GPIO.output(out1,GPIO.LOW)
        GPIO.output(out2,GPIO.HIGH)
        GPIO.output(out3,GPIO.HIGH)
        GPIO.output(out4,GPIO.LOW)
        time.sleep(0.01)
    elif i==4 and var3==True:
        GPIO.output(out1,GPIO.LOW)
        GPIO.output(out2,GPIO.LOW)
        GPIO.output(out3,GPIO.HIGH)
        GPIO.output(out4,GPIO.LOW)
        time.sleep(0.01)
    elif i==5 and var3==True:
        GPIO.output(out1,GPIO.LOW)
        GPIO.output(out2,GPIO.LOW)
        GPIO.output(out3,GPIO.HIGH)
        GPIO.output(out4,GPIO.HIGH)
        time.sleep(0.01)
    elif i==6 and var3==True:    
        GPIO.output(out1,GPIO.LOW)
        GPIO.output(out2,GPIO.LOW)
        GPIO.output(out3,GPIO.LOW)
        GPIO.output(out4,GPIO.HIGH)
        time.sleep(0.01)
    elif i==7 and var3==True:
        GPIO.output(out1,GPIO.HIGH)
        GPIO.output(out2,GPIO.LOW)
        GPIO.output(out3,GPIO.LOW)
        GPIO.output(out4,GPIO.HIGH)
        time.sleep(0.01)


print ("Give some +ve and -ve values in measurement in Cm.....")

try:
   while(1):
      print(m)
      GPIO.output(out1,GPIO.LOW)
      GPIO.output(out2,GPIO.LOW)
      GPIO.output(out3,GPIO.LOW)
      GPIO.output(out4,GPIO.LOW)
        
      print('Type 1 to start')
      z = input()
      p = int(z)
      if p==1:
        for z in range(1000,0,-1):
          x=-1000000
          x=x*-1
          for y in range(x,0,-1):
              var1=GPIO.input(23)
              var2=GPIO.input(24)
              var3=GPIO.input(26)
              m=m-1
              if positive==1:
                  if i==0:
                      i=7
                  else:
                      i=i-1
                  y=y+3
                  positive=0
              negative=1
              if var2==True and var3==True:
                move()
                 # i=i-1


              a = m*0.15
              b = a/10
              print('distance moved is', a, 'mm')
              print('distance moved is', b, 'cm')

              if var2==False:
                GPIO.output(out1,GPIO.HIGH)
                GPIO.output(out2,GPIO.HIGH)
                GPIO.output(out3,GPIO.HIGH)
                GPIO.output(out4,GPIO.HIGH)
                time.sleep(2)
                reference()
                m = 0
                a = 0
                b = 0
                print('Referenced to', a, 'mm')
                print('Referenced to', b, 'cm')
                time.sleep(10)
                break

              if var3==False:  
                GPIO.output(out1,GPIO.HIGH)
                GPIO.output(out2,GPIO.HIGH)
                GPIO.output(out3,GPIO.HIGH)
                GPIO.output(out4,GPIO.HIGH)
                time.sleep(20)
                print('signal cut at', b,'cm')
                break

              if i==0:
                  i=7
                  continue
             # if var1==True:
              i=i-1 
          x=1000000    
          for y in range(x,0,-1):
              var1=GPIO.input(23)
              var2=GPIO.input(24)
              var3=GPIO.input(26)
              m=m+1
              if negative==1:
                  if i==7:
                      i=0
                  else:
                      i=i+1
                  y=y+2
                  negative=0
              positive=1
              if var1==True and var3==True:
                move()

              a = m*0.15
              b = a/10
              print('distance moved is', a, 'mm')
              print('distance moved is', b, 'cm')


              if var1==False:
                GPIO.output(out1,GPIO.HIGH)
                GPIO.output(out2,GPIO.HIGH)
                GPIO.output(out3,GPIO.HIGH)
                GPIO.output(out4,GPIO.HIGH)
                time.sleep(2)
               # time.sleep(10)
                print(m)
              #  m=m-k
                print(m)
                time.sleep(5)
                #reference()
                break

              elif var3==False:  
                GPIO.output(out1,GPIO.HIGH)
                GPIO.output(out2,GPIO.HIGH)
                GPIO.output(out3,GPIO.HIGH)
                GPIO.output(out4,GPIO.HIGH)
                time.sleep(20)
                print('Signal cut at', b, 'cm')
                break


              if i==7:
                  i=0
                  continue
              i=i+1
              
except KeyboardInterrupt:
    GPIO.cleanup()

