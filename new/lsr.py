import time
import VL53L1X
 
# Create a VL53L0X object
tof = VL53L1X.VL53L1X()
 
# Start ranging
tof.start_ranging(VL53L1X.VL53L1X_BETTER_ACCURACY_MODE)
 
timing = tof.get_timing()
if (timing < 20000):
    timing = 20000
print ("Timing %d ms" % (timing/1000))
 
for count in range(1,101):
    distance = tof.get_distance()
    if (distance > 0):
        print ("%d mm, %d cm, %d" % (distance, (distance/10), count))
 
    time.sleep(timing/1000000.00)
 
tof.stop_ranging()
