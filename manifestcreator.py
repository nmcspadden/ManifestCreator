#!/usr/bin/python

# Copyright 2014-2016 Nick McSpadden
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
manifestcreator

Quickly create Munki manifests based on a CSV template.

positional arguments:
  file        Path to the CSV template file.

optional arguments:
  -h, --help  show this help message and exit
"""

import csv
import shutil
import argparse

p = argparse.ArgumentParser(
    description="Quickly create Munki manifests based on a CSV template.")
p.add_argument(
    "file",
    help="Path to the CSV template file.")
arguments = p.parse_args()

with open(arguments.file, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        shutil.copyfile(
            '/Volumes/munki/manifests/Template', '/Volumes/munki/manifests/' + row[0])
