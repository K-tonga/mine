#!/usr/bin/python3

import random

def generate_dummy_data():
	'''Return dummy data as a dictionary with 32 keys (1..32)
	   The value of each key is an array with 16 floating point values 
	'''

	dummy_data = {}

	for num in range(1,32):

		readings = []
		for reading in range(0, 16):
			readings.append(random.random())

		dummy_data[str(num)] = readings

	return dummy_data

