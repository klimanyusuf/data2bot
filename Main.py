#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import jsonschema
import genson
from jsonschema import validate
from genson import SchemaBuilder


#reading the data
builder = SchemaBuilder()
with open('data_1.json', 'r') as f:
    datastore = json.load(f)
    builder.add_object(datastore )
    
#build Schema
builder.to_schema()

#dump data1 to schema1
with open('schema1.json', 'w') as json_file:
    json.dump(schema1, json_file)

#read data 2
builder = SchemaBuilder()
with open('data_2.json', 'r') as r:
    datastore = json.load(r)
    builder.add_object(datastore )
    
#build Schema for data2
builder.to_schema()

#assigning respective schema to new ones built
schema2 = builder.to_schema()
schema1 = builder.to_schema()

# dump data2 to schema 2
with open('schema2.json', 'w') as json_file:
    json.dump(schema2, json_file)

# redefining schema1
schema1 = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "rollnumber": {"type": "number"},
        "marks": {"type": "number"}}}
    
# validating schemas
def validateJson(f):
    try:
        validate(instance=f, schema=schema1)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

#validaing schemas
isValid = validateJson(f)
if isValid:
    print(f)
    print("Given JSON data is True")
else:
    print(f)
    print("Given JSON data is False")

    
#do the same for schema 2
schema2 = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "rollnumber": {"type": "number"},
        "marks": {"type": "number"}}}


# 

def validateJson(r):
    try:
        validate(instance=r, schema=schema1)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True


# In[52]:


isValid = validateJson(f)
if isValid:
    print(f)
    print("Given JSON data is True")
else:
    print(f)
    print("Given JSON data is False")
