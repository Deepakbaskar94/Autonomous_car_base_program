import RPi.GPIO as GPIO
import time
import subprocess
import tempfile
import os
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

#while True:
print("LED ON")
GPIO.output(18, GPIO.HIGH)
print("wait")
time.sleep(1)
#time.sleep(1)
print("LED OFF")
GPIO.output(18,GPIO.LOW)
print("wait")
time.sleep(1)
#time.sleep(1)
print("stop")

#with tempfile.TemporaryFile() as tempf:
   # proc = subprocess.Popen(['adb', 'shell', 'dumpsys', 'battery'], stdout=tempf)
   # proc.wait()
   # tempf.seek(0)
   # print tempf.read()
while True:
#cmd = ['adb', 'shell', 'dumpsys', 'battery', '|', 'grep', 'level', '|', 'awk', '{print $4}']
    command = "adb shell dumpsys battery | grep level | awk '{print $2}' "
#os.system(cmd)
#output = subprocess.Popen( cmd, stdout=subprocess.PIPE,shell=False ).communicate()[0]
    output = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#print(output)
    strbattery = str(output.communicate()[0]).split("'")[1].split("\\")[0]
    print(strbattery)

    battery = int(strbattery)
    if battery > 50:
        print("battery is sufficiently charged")
        print("switch off the charger")
        GPIO.output(18, GPIO.LOW)
        print("OFF")

    elif battery == 50:
        print("charging is going to off")

    elif battery < 50:
        print("switch on the charger")
        GPIO.output(18, GPIO.HIGH)
        print("ON")

    else:
        print("do nothing")

    time.sleep(10)
