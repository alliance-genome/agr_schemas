
[![Build Status](https://travis-ci.org/alliance-genome/agr_schemas.svg?branch=development)](https://travis-ci.org/alliance-genome/agr_schemas)
[![Build Status](https://travis-ci.org/alliance-genome/agr_schemas.svg?branch=master)](https://travis-ci.org/alliance-genome/agr_schemas)

Alliance JSON Ingest Schemas and Data Dictionary
================

This directory contains JSON schemas used to define data for integration into the Alliance of Genome Resources and defines the data dictionary of the Alliance data store.


Validation
----------
The python script "agr_validate.py" can be used to validate a JSON entry against a schema for testing/development purposes.
Usage is as follows: 
`agr_validate.py -d test_data.json -s base_schema.json`

For the basic Gene info file run
   `./agr_validate.py -d <your_new_gene_file.json> -s  gene/geneMetaData.json`
for the disease info file run
   `./agr_validate.py -d <your_new_disease_file.json> -s  disease/diseaseMetaDataDefinition.json`
and for the allele info file run
   `./agr_validate.py -d <your_new_allele_file.json> -s  allele/alleleMetaData.json`

The java script "agr_validate_schema.sh" can be used to validate that the schema file itself conforms to the draft-4 version of the JSON schema spec and will run on PR into master.  

For validating all schema files in a branch: 
`./agr_validate_schema.sh`


GOCD Validation
---------------

JSON schema files are validated by the Continuous Integration / Deployment System (GOCD) through a JAVA JSON validator made available through the Docker base container. This is because the JAVA implementation is much more strict than the Python implementation. This validation is called by the default command in the Docker files. The way the java works is that the Dockerfile points to a directory full of JSON files. Java opens each file and checks for the "$schema": "http://json-schema.org/draft-04/schema#", property if its found then it validates it, otherwise ignores the file. 

In order to run these validations locally install Docker and then run the command:

```bash
make run
```

Data Dictionary
---------------

The Alliance Data Dictionary is a set of information that describes the content, format and structure of the nodes and relations in the Alliance data store. metaschema.yaml defines the potential content of each sub-schema.  Each file is named according to its corresponding node label.  

