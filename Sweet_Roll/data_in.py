#!/usr/bin/env python3

# Script that reads and plots accel and gyro data from a serial port.
# Author: zabuelhaj

import serial
import numpy as np
import matplotlib

def connectDevice():
	"""
	Opens a serial port to access microcontroller data.
	Parameters: None
	Returns: Serial port
	"""
	ser = serial.Serial("/dev/ttyUSB0", 57600)
	print("Connected to device: ", ser.name)
	return ser

def main():
	ser = connectDevice()

	# Testing:
	while True:
		print(ser.read(1))

if __name__=='__main__':
	main()