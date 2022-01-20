#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import jsonschema
import genson
from jsonschema import validate
from genson import SchemaBuilder


# In[8]:


with open('data_1.json', 'r') as f:
    datastore = json.load(f)
    datastore


# In[9]:


builder = SchemaBuilder()
with open('data_1.json', 'r') as f:
    datastore = json.load(f)
    builder.add_object(datastore )

builder.to_schema()


# In[ ]:


with open('schema1.json', 'w') as json_file:
    json.dump(schema1, json_file)


# In[44]:


builder = SchemaBuilder()
with open('data_2.json', 'r') as r:
    datastore = json.load(r)
    builder.add_object(datastore )

builder.to_schema()


# In[47]:


schema2 = builder.to_schema()
schema1 = builder.to_schema()


# In[48]:


with open('schema2.json', 'w') as json_file:
    json.dump(schema2, json_file)


# In[ ]:





# In[49]:


schema1 = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "rollnumber": {"type": "number"},
        "marks": {"type": "number"}}}
    


# In[50]:


def validateJson(f):
    try:
        validate(instance=f, schema=schema1)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True


# In[53]:


isValid = validateJson(f)
if isValid:
    print(f)
    print("Given JSON data is True")
else:
    print(f)
    print("Given JSON data is False")


# In[ ]:





# In[ ]:


schema2 = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "rollnumber": {"type": "number"},
        "marks": {"type": "number"}}}


# In[51]:


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


# In[ ]:





# In[26]:



isValid = validateJson(f)
if isValid:
    print(f)
    print("Given JSON data is Valid")
else:
    print(f)
    print("Given JSON data is InValid")


# In[ ]:





# In[40]:





# In[ ]:




