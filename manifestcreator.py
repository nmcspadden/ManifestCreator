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
  file                 Path to the CSV template file.

optional arguments:
  -h, --help           show this help message and exit
  -v, --verbose        Outputs the path to each manifest as it is created.
  --repo REPO          The path to the Munki repository you want to add
                       manifests to. Defaults to /Volumes/munki.
  --template TEMPLATE  The path to the file you want to use as your manifest
                       template. Defaults to
                       /Volumes/munki/manifests/Template.
"""

import csv
import shutil
import argparse

p = argparse.ArgumentParser(
    description="Quickly create Munki manifests based on a CSV template.")
p.add_argument(
    "file",
    help="Path to the CSV template file.")
p.add_argument(
    "-v", "--verbose",
    action="store_true",
    help="Outputs the path to each manifest as it is created.")
p.add_argument(
    "--repo",
    action="store",
    help=("The path to the Munki repository you want to add manifests to. "
          "Defaults to /Volumes/munki."))
p.add_argument(
    "--template",
    action="store",
    help=("The path to the file you want to use as your manifest template. "
          "Defaults to /Volumes/munki/manifests/Template."))
arguments = p.parse_args()

if arguments.repo:
    repo = arguments.repo
else:
    repo = "/Volumes/munki"

if arguments.template:
    template = arguments.template
else:
    template = repo + "/manifests/Template"

with open(arguments.file, "rb") as f:
    reader = csv.reader(f)
    for row in reader:
        shutil.copyfile(
            template, repo + "/manifests/" + row[0])
        if arguments.verbose is True:
            print repo + "/manifests/" + row[0]
