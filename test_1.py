from factory.parsers import serializer, jsonparser, yamlparser, tomlparser
from math import sin

def func():
    return 2

#jsonparser.dump(serializer.serialize_obj(func), 'temp.json')

try:
    jsonparser.load('temp.json')
except KeyError:
    print('key bruhhh')
except ValueError:
    print('Valuebruhh bruhhh')


pass
