#!/usr/bin/env python 
import yaml 
import os
import argparse

parser = argparse.ArgumentParser(description='This is a simple validator for resourceDescriptors.yaml.')

parser.add_argument('-d','--data', help='resourceDescriptor.yaml',required=True)
args = parser.parse_args()

data_file_name = args.data
with open(data_file_name) as data_file:
    try: 
        data = yaml.load(data_file)
        #print(yaml.dump(data))
        print ("successfully validated " + args.data)
    except yaml.YAMLError as exc:
        print (exc)
