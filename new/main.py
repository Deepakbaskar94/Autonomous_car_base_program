import Adafruit_BBIO.GPIO as GPIO
from time import sleep
import sys
import ctypes, os

class timespec(ctypes.Structure):
        _fields_ =\
        [
            ('tv_sec', ctypes.c_long),
            ('tv_nsec', ctypes.c_long)
        ]



CLOCK_MONOTONIC_RAW = 4
librt = ctypes.CDLL('librt.so.1', use_errno=True)
clock_gettime = librt.clock_gettime
#specify input arguments and types to the C clock_gettime() function
# (int clock_ID, timespec* t)
clock_gettime.argtypes = [ctypes.c_int, ctypes.POINTER(timespec)]



class Stepper:
    # poweron = 0
	def __init__(self):
		self.step_number = 0    # which step the motor is on
		self.direction = 0      # motor direction
		self.last_step_time = 0 # time stamp in us of the last step taken
		self.number_of_steps = 0 # total number of steps for this motor
		self.step_delay = 0

		# Arduino pins for the motor control connection:
		self.motor_pin_1 = 0
		self.motor_pin_2 = 0
		self.motor_pin_3 = 0
		self.motor_pin_4 = 0
		self.motor_pin_5 = 0
		self.pin_count = 4

	def monotonic_time(self):

		t = timespec()
		#(Note that clock_gettime() returns 0 for success, or -1 for failure, in
		# which case errno is set appropriately)
		#-see here: http://linux.die.net/man/3/clock_gettime
		if clock_gettime(CLOCK_MONOTONIC_RAW , ctypes.pointer(t)) != 0:
			#if clock_gettime() returns an error
			errno_ = ctypes.get_errno()
			raise OSError(errno_, os.strerror(errno_))
		return t.tv_sec + t.tv_nsec*1e-9  #sec

	def micros(self):

		return self.monotonic_time()*1e6  #us

	def millis(self):

		return self.monotonic_time()*1e3  #ms



	def Stepper_setup(self,number_of_steps,motor_pin_1,motor_pin_2,motor_pin_3,motor_pin_4):

		self.step_number = 0    # which step the motor is on
		self.direction = 0      # motor direction
		self.last_step_time = 0 # time stamp in us of the last step taken
		self.number_of_steps = number_of_steps # total number of steps for this motor

		# Arduino pins for the motor control connection:
		self.motor_pin_1 = motor_pin_1
		self.motor_pin_2 = motor_pin_2
		self.motor_pin_3 = motor_pin_3
		self.motor_pin_4 = motor_pin_4

		#setup the pins on the microcontroller:
		GPIO.setup(self.motor_pin_1, GPIO.OUT)
		GPIO.setup(self.motor_pin_2, GPIO.OUT)
		GPIO.setup(self.motor_pin_3, GPIO.OUT)
		GPIO.setup(self.motor_pin_4, GPIO.OUT)

		#When there are 4 pins, set the others to 0:
		self.motor_pin_5 = 0
		#pin_count is used by the stepMotor() method:
		self.pin_count = 4


	def setSpeed(self,whatSpeed):
		self.step_delay = 60L * 1000L * 1000L / self.number_of_steps / whatSpeed
	
	def step(self,steps_to_move):

		steps_left = abs(steps_to_move)  # how many steps to take

		# determine direction based on whether steps_to_mode is + or -:
		if (steps_to_move > 0):
			self.direction = 1
		if (steps_to_move < 0):
			self.direction = 0


		# decrement the number of steps, moving one step each time:
		while (steps_left > 0):

			now = self.micros()

			# move only if the appropriate delay has passed:
			if (now - self.last_step_time >= self.step_delay):

				# get the timeStamp of when you stepped:
				self.last_step_time = now
				# increment or decrement the step number,
				# depending on direction:
				if (self.direction == 1):

					self.step_number += 1
					if (self.step_number == self.number_of_steps):
					  	self.step_number = 0

				else:

					if (self.step_number == 0):
					  	self.step_number = self.number_of_steps
					self.step_number -=1

				# decrement the steps left:
				steps_left-=1
				# step the motor to step number 0, 1, ..., {3 or 10}
				if (self.pin_count == 5):
					self.stepMotor(self.step_number % 10)
				else:
					self.stepMotor(self.step_number % 4)


	def stepMotor(self,thisStep):

		if (self.pin_count == 2):

			if(thisStep == 0):  # 01
				GPIO.output(self.motor_pin_1, GPIO.LOW)
				GPIO.output(self.motor_pin_2, GPIO.HIGH)

			if(thisStep == 1):  # 11
				GPIO.output(self.motor_pin_1, GPIO.HIGH)
				GPIO.output(self.motor_pin_2, GPIO.HIGH)

			if(thisStep == 2):  # 10
				GPIO.output(self.motor_pin_1, GPIO.HIGH)
				GPIO.output(self.motor_pin_2, GPIO.LOW)

			if(thisStep == 3):  # 00
				GPIO.output(self.motor_pin_1, GPIO.LOW)
				GPIO.output(self.motor_pin_2, GPIO.LOW)


		if (self.pin_count == 4):

			if(thisStep == 0):  # 1010
				GPIO.output(self.motor_pin_1, GPIO.HIGH)
				GPIO.output(self.motor_pin_2, GPIO.LOW)
				GPIO.output(self.motor_pin_3, GPIO.HIGH)
				GPIO.output(self.motor_pin_4, GPIO.LOW)

			if(thisStep == 1):  # 0110
				GPIO.output(self.motor_pin_1, GPIO.LOW)
				GPIO.output(self.motor_pin_2, GPIO.HIGH)
				GPIO.output(self.motor_pin_3, GPIO.HIGH)
				GPIO.output(self.motor_pin_4, GPIO.LOW)

			if(thisStep == 2):  # 0101
				GPIO.output(self.motor_pin_1, GPIO.LOW)
				GPIO.output(self.motor_pin_2, GPIO.HIGH)
				GPIO.output(self.motor_pin_3, GPIO.LOW)
				GPIO.output(self.motor_pin_4, GPIO.HIGH)

			if(thisStep == 3):  # 1001
				GPIO.output(self.motor_pin_1, GPIO.HIGH)
				GPIO.output(self.motor_pin_2, GPIO.LOW)
				GPIO.output(self.motor_pin_3, GPIO.LOW)
				GPIO.output(self.motor_pin_4, GPIO.HIGH)


		if (self.pin_count == 5):

			if(thisStep == 0):  # 01101
				GPIO.output(self.motor_pin_1, GPIO.LOW)
				GPIO.output(self.motor_pin_2, GPIO.HIGH)
				GPIO.output(self.motor_pin_3, GPIO.HIGH)
				GPIO.output(self.motor_pin_4, GPIO.LOW)
				GPIO.output(self.motor_pin_5, GPIO.HIGH)

			if(thisStep == 1):  # 01001
				GPIO.output(self.motor_pin_1, GPIO.LOW)
				GPIO.output(self.motor_pin_2, GPIO.HIGH)
				GPIO.output(self.motor_pin_3, GPIO.LOW)
				GPIO.output(self.motor_pin_4, GPIO.LOW)
				GPIO.output(self.motor_pin_5, GPIO.HIGH)

			if(thisStep == 2):  # 01011
				GPIO.output(self.motor_pin_1, GPIO.LOW)
				GPIO.output(self.motor_pin_2, GPIO.HIGH)
				GPIO.output(self.motor_pin_3, GPIO.LOW)
				GPIO.output(self.motor_pin_4, GPIO.HIGH)
				GPIO.output(self.motor_pin_5, GPIO.HIGH)

			if(thisStep == 3):  # 01010
				GPIO.output(self.motor_pin_1, GPIO.LOW)
				GPIO.output(self.motor_pin_2, GPIO.HIGH)
				GPIO.output(self.motor_pin_3, GPIO.LOW)
				GPIO.output(self.motor_pin_4, GPIO.HIGH)
				GPIO.output(self.motor_pin_5, GPIO.LOW)

			if(thisStep == 4):  # 11010
				GPIO.output(self.motor_pin_1, GPIO.HIGH)
				GPIO.output(self.motor_pin_2, GPIO.HIGH)
				GPIO.output(self.motor_pin_3, GPIO.LOW)
				GPIO.output(self.motor_pin_4, GPIO.HIGH)
				GPIO.output(self.motor_pin_5, GPIO.LOW)

			if(thisStep == 5):  # 10010
				GPIO.output(self.motor_pin_1, GPIO.HIGH)
				GPIO.output(self.motor_pin_2, GPIO.LOW)
				GPIO.output(self.motor_pin_3, GPIO.LOW)
				GPIO.output(self.motor_pin_4, GPIO.HIGH)
				GPIO.output(self.motor_pin_5, GPIO.LOW)

			if(thisStep == 6):  # 10110
				GPIO.output(self.motor_pin_1, GPIO.HIGH)
				GPIO.output(self.motor_pin_2, GPIO.LOW)
				GPIO.output(self.motor_pin_3, GPIO.HIGH)
				GPIO.output(self.motor_pin_4, GPIO.HIGH)
				GPIO.output(self.motor_pin_5, GPIO.LOW)

			if(thisStep == 7):  # 10100
				GPIO.output(self.motor_pin_1, GPIO.HIGH)
				GPIO.output(self.motor_pin_2, GPIO.LOW)
				GPIO.output(self.motor_pin_3, GPIO.HIGH)
				GPIO.output(self.motor_pin_4, GPIO.LOW)
				GPIO.output(self.motor_pin_5, GPIO.LOW)

			if(thisStep == 8):  # 10101
				GPIO.output(self.motor_pin_1, GPIO.HIGH)
				GPIO.output(self.motor_pin_2, GPIO.LOW)
				GPIO.output(self.motor_pin_3, GPIO.HIGH)
				GPIO.output(self.motor_pin_4, GPIO.LOW)
				GPIO.output(self.motor_pin_5, GPIO.HIGH)

			if(thisStep == 9):  # 00101
				GPIO.output(self.motor_pin_1, GPIO.LOW)
				GPIO.output(self.motor_pin_2, GPIO.LOW)
				GPIO.output(self.motor_pin_3, GPIO.HIGH)
				GPIO.output(self.motor_pin_4, GPIO.LOW)
				GPIO.output(self.motor_pin_5, GPIO.HIGH)





if __name__ == "__main__":

	stepsPerRevolution = 200
	in1 = "P8_8"
	in2 = "P8_10"
	in3 = "P8_12"
	in4 = "P8_14"
	x= Stepper()
	x.Stepper_setup(stepsPerRevolution, in1, in2, in3, in4)
	x.setSpeed(260)


	#        for i in range(12):
	#             	print("clockwise")


	#                x.step(stepsPerRevolution)

	#        sleep(1)

	#        for i in range(12):
	#                print("counterclockwise")
	#                x.step(-stepsPerRevolution)





	while(True):
		#print("clockwise")
		#x.step(stepsPerRevolution)
		#x.step(stepsPerRevolution)
		for i in range(12):
			print("clockwise")

			x.step(stepsPerRevolution)

		sleep(1)

		for i in range(12):
			print("counterclockwise")
			x.step(-stepsPerRevolution)
		#print("counterclockwise")

		#x.step(-stepsPerRevolution)
		#x.step(-stepsPerRevolution)

		sleep(1)
		#
