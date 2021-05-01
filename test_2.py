from factory.Factory import Factory
from factory.parsers import serializer

p = Factory.get_parser("json")

g = serializer.deserialize_obj(p.load("temp.json"))

print(g(15))
