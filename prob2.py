#!/usr/bin/python3

import glob
import datetime
import prob1

def get_timestamp():
	'''Return a timestamp adding a suffix incase
	   a file already exists with that timestamp.
	'''
	timestamp = str(datetime.datetime.now())
	timestamp = timestamp.replace("-", ".")
	timestamp = timestamp.replace(":", ".")
	timestamp = timestamp.replace(" ", ".")

	suffix = ""

	existing = glob.glob(timestamp + "*")
	if (len(existing) > 0):
		suffix = "_" + str(len(existing) + 1)
	
	timestamp += suffix;

	return timestamp

def store_dataset(dataset):
	'''Write the dataset to a text file, taking care not to overwrite
	   any existing datasets
	'''

	timestamp = get_timestamp()

	with open(timestamp, "w") as out_f:

		for key in sorted(dataset.keys(), key=int):

			readings = ",".join(str(x) for x in dataset[key])

			print(key + ":" + readings, file=out_f)

	return 1


