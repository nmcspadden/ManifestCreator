#!/usr/bin/python

import csv
import shutil
import argparse

p = argparse.ArgumentParser()
p.add_argument("file")
arguments = p.parse_args()

with open(arguments.file, 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		shutil.copyfile('/Volumes/munki/manifests/Template','/Volumes/munki/manifests/' + row[0])

