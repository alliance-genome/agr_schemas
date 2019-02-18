#!/usr/bin/env python
import json
import strict_rfc3339
import os
import argparse
import sys
import jsonschema as js

parser = argparse.ArgumentParser(description='This is a simple validator for JSON schema.')

parser.add_argument('-d','--data', help='JSON data file',required=True)
parser.add_argument('-s','--schema',help='JSON schema file', required=True)
args = parser.parse_args() 

data_file_name = args.data
with open(data_file_name) as data_file:
    data = json.load(data_file)
data_file.closed

schema_file_name = args.schema
with open(schema_file_name) as schema_file:
    schema = json.load(schema_file)
    print(schema)
schema_file.closed

# Defining a resolver for relative paths and schema issues, see https://github.com/Julian/jsonschema/issues/313
# and https://github.com/Julian/jsonschema/issues/274
sSchemaDir = os.path.dirname(os.path.abspath(schema_file_name))
oResolver = js.RefResolver(base_uri = 'file://' + sSchemaDir + '/', referrer = schema)

print(oResolver)
print ("schemaDir: " + sSchemaDir)
print ("schema_file_name: " + schema_file_name)

try:
    js.validate(data, schema, format_checker=js.FormatChecker(), resolver=oResolver)
    print "'%s' successfully validated against '%s'" % (data_file_name, schema_file_name)
except js.ValidationError as e:
    print e.message
    print e
    raise SystemExit("Error in validation.")
except js.SchemaError as e:
    print e.message
    print e
    raise SystemExit("Error in schema validation.")
