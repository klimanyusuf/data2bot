{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "import jsonschema\n",
    "import genson\n",
    "from jsonschema import validate\n",
    "from genson import SchemaBuilder"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'$schema': 'http://json-schema.org/schema#',\n",
       " 'type': 'object',\n",
       " 'properties': {'attributes': {'type': 'object',\n",
       "   'properties': {'appName': {'type': 'string'},\n",
       "    'eventType': {'type': 'string'},\n",
       "    'subEventType': {'type': 'string'},\n",
       "    'sensitive': {'type': 'boolean'}},\n",
       "   'required': ['appName', 'eventType', 'sensitive', 'subEventType']},\n",
       "  'message': {'type': 'object',\n",
       "   'properties': {'battle': {'type': 'object',\n",
       "     'properties': {'id': {'type': 'string'},\n",
       "      'name': {'type': 'string'},\n",
       "      'orientation': {'type': 'string'},\n",
       "      'settings': {'type': 'object',\n",
       "       'properties': {'minParticipants': {'type': 'integer'},\n",
       "        'maxParticipants': {'type': 'integer'},\n",
       "        'battleType': {'type': 'string'},\n",
       "        'wagerType': {'type': 'string'},\n",
       "        'countdown': {'type': 'integer'},\n",
       "        'duration': {'type': 'integer'},\n",
       "        'archetype': {'type': 'object',\n",
       "         'properties': {'name': {'type': 'string'},\n",
       "          'iconId': {'type': 'string'}},\n",
       "         'required': ['iconId', 'name']}},\n",
       "       'required': ['archetype',\n",
       "        'battleType',\n",
       "        'countdown',\n",
       "        'duration',\n",
       "        'maxParticipants',\n",
       "        'minParticipants',\n",
       "        'wagerType']},\n",
       "      'status': {'type': 'string'},\n",
       "      'creationTime': {'type': 'integer'},\n",
       "      'startTime': {'type': 'integer'},\n",
       "      'endTime': {'type': 'integer'},\n",
       "      'creator': {'type': 'object',\n",
       "       'properties': {'id': {'type': 'string'},\n",
       "        'nickname': {'type': 'string'},\n",
       "        'title': {'type': 'string'},\n",
       "        'accountType': {'type': 'string'},\n",
       "        'countryCode': {'type': 'string'},\n",
       "        'orientation': {'type': 'string'}},\n",
       "       'required': ['accountType',\n",
       "        'countryCode',\n",
       "        'id',\n",
       "        'nickname',\n",
       "        'orientation',\n",
       "        'title']},\n",
       "      'participants': {'type': 'array',\n",
       "       'items': {'type': 'object',\n",
       "        'properties': {'user': {'type': 'object',\n",
       "          'properties': {'id': {'type': 'string'},\n",
       "           'nickname': {'type': 'string'},\n",
       "           'title': {'type': 'string'},\n",
       "           'accountType': {'type': 'string'},\n",
       "           'countryCode': {'type': 'string'},\n",
       "           'orientation': {'type': 'string'}},\n",
       "          'required': ['accountType',\n",
       "           'countryCode',\n",
       "           'id',\n",
       "           'nickname',\n",
       "           'orientation',\n",
       "           'title']},\n",
       "         'creator': {'type': 'boolean'},\n",
       "         'ranking': {'type': 'integer'},\n",
       "         'numberOfTrades': {'type': 'integer'},\n",
       "         'performance': {'type': 'string'}},\n",
       "        'required': ['creator',\n",
       "         'numberOfTrades',\n",
       "         'performance',\n",
       "         'ranking',\n",
       "         'user']}}},\n",
       "     'required': ['creationTime',\n",
       "      'creator',\n",
       "      'endTime',\n",
       "      'id',\n",
       "      'name',\n",
       "      'orientation',\n",
       "      'participants',\n",
       "      'settings',\n",
       "      'startTime',\n",
       "      'status']},\n",
       "    'joiner': {'type': 'object',\n",
       "     'properties': {'id': {'type': 'string'},\n",
       "      'nickname': {'type': 'string'},\n",
       "      'title': {'type': 'string'},\n",
       "      'accountType': {'type': 'string'},\n",
       "      'countryCode': {'type': 'string'},\n",
       "      'orientation': {'type': 'string'}},\n",
       "     'required': ['accountType',\n",
       "      'countryCode',\n",
       "      'id',\n",
       "      'nickname',\n",
       "      'orientation',\n",
       "      'title']},\n",
       "    'participantIds': {'type': 'array', 'items': {'type': 'string'}}},\n",
       "   'required': ['battle', 'joiner', 'participantIds']}},\n",
       " 'required': ['attributes', 'message']}"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "builder = SchemaBuilder()\n",
    "with open('data_1.json', 'r') as f:\n",
    "    datastore = json.load(f)\n",
    "    builder.add_object(datastore )\n",
    "\n",
    "builder.to_schema()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('schema1.json', 'w') as json_file:\n",
    "    json.dump(schema1, json_file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'$schema': 'http://json-schema.org/schema#',\n",
       " 'type': 'object',\n",
       " 'properties': {'attributes': {'type': 'object',\n",
       "   'properties': {'appName': {'type': 'string'},\n",
       "    'eventType': {'type': 'string'},\n",
       "    'subEventType': {'type': 'string'},\n",
       "    'sensitive': {'type': 'boolean'}},\n",
       "   'required': ['appName', 'eventType', 'sensitive', 'subEventType']},\n",
       "  'message': {'type': 'object',\n",
       "   'properties': {'user': {'type': 'object',\n",
       "     'properties': {'id': {'type': 'string'},\n",
       "      'nickname': {'type': 'string'},\n",
       "      'title': {'type': 'string'},\n",
       "      'accountType': {'type': 'string'},\n",
       "      'countryCode': {'type': 'string'},\n",
       "      'orientation': {'type': 'string'}},\n",
       "     'required': ['accountType',\n",
       "      'countryCode',\n",
       "      'id',\n",
       "      'nickname',\n",
       "      'orientation',\n",
       "      'title']},\n",
       "    'time': {'type': 'integer'},\n",
       "    'acl': {'type': 'array'},\n",
       "    'publicFeed': {'type': 'boolean'},\n",
       "    'internationalCountries': {'type': 'array', 'items': {'type': 'string'}},\n",
       "    'topTraderFeed': {'type': 'boolean'}},\n",
       "   'required': ['acl',\n",
       "    'internationalCountries',\n",
       "    'publicFeed',\n",
       "    'time',\n",
       "    'topTraderFeed',\n",
       "    'user']}},\n",
       " 'required': ['attributes', 'message']}"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "builder = SchemaBuilder()\n",
    "with open('data_2.json', 'r') as r:\n",
    "    datastore = json.load(r)\n",
    "    builder.add_object(datastore )\n",
    "\n",
    "builder.to_schema()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "schema2 = builder.to_schema()\n",
    "schema1 = builder.to_schema()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('schema2.json', 'w') as json_file:\n",
    "    json.dump(schema2, json_file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "schema1 = {\n",
    "    \"type\": \"object\",\n",
    "    \"properties\": {\n",
    "        \"name\": {\"type\": \"string\"},\n",
    "        \"rollnumber\": {\"type\": \"number\"},\n",
    "        \"marks\": {\"type\": \"number\"}}}\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "def validateJson(f):\n",
    "    try:\n",
    "        validate(instance=f, schema=schema1)\n",
    "    except jsonschema.exceptions.ValidationError as err:\n",
    "        return False\n",
    "    return True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<_io.TextIOWrapper name='data_1.json' mode='r' encoding='cp1252'>\n",
      "Given JSON data is False\n"
     ]
    }
   ],
   "source": [
    "isValid = validateJson(f)\n",
    "if isValid:\n",
    "    print(f)\n",
    "    print(\"Given JSON data is True\")\n",
    "else:\n",
    "    print(f)\n",
    "    print(\"Given JSON data is False\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "schema2 = {\n",
    "    \"type\": \"object\",\n",
    "    \"properties\": {\n",
    "        \"name\": {\"type\": \"string\"},\n",
    "        \"rollnumber\": {\"type\": \"number\"},\n",
    "        \"marks\": {\"type\": \"number\"}}}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [],
   "source": [
    "def validateJson(r):\n",
    "    try:\n",
    "        validate(instance=r, schema=schema1)\n",
    "    except jsonschema.exceptions.ValidationError as err:\n",
    "        return False\n",
    "    return True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<_io.TextIOWrapper name='data_1.json' mode='r' encoding='cp1252'>\n",
      "Given JSON data is False\n"
     ]
    }
   ],
   "source": [
    "isValid = validateJson(f)\n",
    "if isValid:\n",
    "    print(f)\n",
    "    print(\"Given JSON data is True\")\n",
    "else:\n",
    "    print(f)\n",
    "    print(\"Given JSON data is False\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<_io.TextIOWrapper name='data_1.json' mode='r' encoding='cp1252'>\n",
      "Given JSON data is InValid\n"
     ]
    }
   ],
   "source": [
    "\n",
    "isValid = validateJson(f)\n",
    "if isValid:\n",
    "    print(f)\n",
    "    print(\"Given JSON data is Valid\")\n",
    "else:\n",
    "    print(f)\n",
    "    print(\"Given JSON data is InValid\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
