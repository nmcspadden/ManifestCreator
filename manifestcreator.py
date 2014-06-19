#!/usr/bin/python

import csv
import subprocess
import shutil

with open('serials.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		shutil.copyfile('/Volumes/munki/manifests/Template','/Volumes/munki/manifests/' + row[0])
