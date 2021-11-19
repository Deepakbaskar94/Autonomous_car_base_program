#!/usr/bin/env python3

"""
servo_test.py
www.bluetin.io
16/01/2018
"""

__author__ = "Mark Heywood"
__version__ = "0.01"
__license__ = "MIT"

from gpiozero import Servo
from time import sleep

# Adjust the pulse values to set rotation range
min_pulse = 0.000544	# Library default = 1/1000
max_pulse = 0.0024		# Library default = 2/1000
# Initial servo position
pos = 0
test = 0
tet = 0


servo = Servo(23, pos, min_pulse, max_pulse, 20/1000, None)

while True:
    tet = input()
    test = int(tet)
    while test < 20:
        pos = test * 0.1 - 1
        servo.value = pos
        print(pos)
        test = test + 1
        sleep(0.05)
		
    while test > 0:
        pos = test * 0.1 - 1 
        servo.value = pos
        print(pos)
        test = test - 1
        sleep(0.05)

