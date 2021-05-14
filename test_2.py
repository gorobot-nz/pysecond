from factory.Factory import Factory
from factory.parsers import serializer

p = Factory.get_parser("yaml")

g = serializer.deserialize_obj(p.load("serialized_file.yaml"))

print(g(15))
