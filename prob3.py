#!/usr/bin/python3

import random

def generate_dummy_data(with_err=False):
	'''Return dummy data as a dictionary with 32 keys (1..32)
	   The value of each key is an array with 16 floating point values 
	'''

	dummy_data = {}

	for num in range(1,32):

		readings = []
		for reading in range(0, 16):

			reading_val = random.random();

			if (with_err):
				#1/3 chance of generating an error
				if (random.randint(0,9) % 3 == 0):
					reading_val = "err"

			readings.append(reading_val)

		dummy_data[str(num)] = readings

	return dummy_data


