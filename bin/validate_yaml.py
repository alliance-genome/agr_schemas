#!/usr/bin/env python
import yaml
import os
import sys
import glob
import base64
import argparse

parser = argparse.ArgumentParser(description='This is a simple validator for all yaml files in repo')
parser.add_argument('file',
                    nargs='?',
                    type=argparse.FileType('r'),
                    #dest="file",
                    default=sys.stdin,
                    help='Use this flag to specify a specific file')
args = parser.parse_args()

if not args.file.name == '<stdin>':
    yaml_filepaths = [args.file.name]
else:
    yaml_filepaths = [y for x in os.walk(os.getcwd()) for y in glob.glob(os.path.join(x[0], '*.yaml'))]

for yaml_filepath in yaml_filepaths:
    print("Validating " + yaml_filepath)
    with open(yaml_filepath, "r") as file_stream:
        yaml_data = file_stream.readlines()
        data = yaml.safe_load("".join(yaml_data))
        print ("Valid YAML")
