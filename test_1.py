from factory.parsers import serializer, jsonparser, yamlparser, tomlparser
from math import sin

try:
    jsonparser.load('temp.json')
except KeyError:
    print('key bruhhh')
except ValueError:
    print('Valuebruhh bruhhh')


pass
