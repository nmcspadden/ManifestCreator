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
import argparse
import plistlib

p = argparse.ArgumentParser(
    description=("A tool that allows Munki administrators to quickly create "
                 "manifests based on a CSV containing serial numbers."))
p.add_argument(
    "file",
    help="Path to the CSV file containing serial numbers.")
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

try:
    manifest_dict = plistlib.readPlist(template)
except:
    print "Manifest template might not be a valid plist file."
    raise

with open(arguments.file, "rb") as f:
    reader = csv.DictReader(f)
    for row in reader:
        new_manifest = repo + "/manifests/" + row["serial"]
        for key in row:
            if key != "serial":
                manifest_dict[key] = row[key]
        plistlib.writePlist(manifest_dict, new_manifest)
        if arguments.verbose is True:
            print new_manifest
