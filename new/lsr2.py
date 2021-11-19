import time
import sys
import signal
import VL53L1X
 
# Create a VL53L0X object
tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0X29)
 
tof.open()
# Start ranging
tof.start_ranging(2)
 
running = True 

timing = tof.get_timing()

def exit_handler(signal, frame):
    global running
    running = False
    top.stop_ranging()
    print()
    sys.exit(0)


if (timing < 20000):
    timing = 20000
print ("Timing %d ms" % (timing/1000))
 
for count in range(1,101):
    distance = tof.get_distance()
    if (distance > 0):
        print ("%d mm, %d cm, %d" % (distance, (distance/10), count))
    elif (distance < 0):
        print("no input")
    time.sleep(timing/1000000.00)


'''while running:
    distance_in_mm = tof.get_distance()
    timing = tof.get_timing()
    print("Distance: {}".format(distance_in_mm))
    time.sleep(1)
    print(timing)'''
 
tof.stop_ranging()
