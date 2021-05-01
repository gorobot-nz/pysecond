from factory.Factory import Factory
from factory.parsers import serializer


def func(num):
    num += 10
    return num ** 2


p = Factory.get_parser("json")

p.dump(serializer.serialize_obj(func), "temp.json")
