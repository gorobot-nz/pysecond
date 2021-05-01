from factory.parsers import jsonparser
from factory.parsers import tomlparser
from factory.parsers import yamlparser
from factory.parsers import pickleparser
from factory.parsers import serializer
from tests.test_funcs import fib, func_2, another_func


def recursive():
    temp = serializer.deserialize_obj(jsonparser.load("test.json"))
    assert temp(10) == fib(10)


def simple():
    temp = serializer.deserialize_obj(tomlparser.load("test.toml"))
    assert temp(18) == func_2(18)


def lambda_():
    k = lambda x, y: x**y
    temp = serializer.deserialize_obj(yamlparser.load("test.yaml"))
    assert k(5, 5) == temp(5, 5)


def onemoretest():
    temp = serializer.deserialize_obj(pickleparser.load("test.pickle"))
    assert another_func(10) == temp(10)


def dictjsontest():
    a = dict()
    b = dict()
    c = dict()
    a['a1'] = 15
    a['a2'] = 15.99
    a['a3'] = None
    a['a4'] = 'hello, its me from A'
    b['b1'] = 15
    b['b2'] = 15.99
    b['b3'] = None
    b['b4'] = 'hello, its me from A'
    c['c1'] = 15
    c['c2'] = 15.99
    c['c3'] = None
    c['c4'] = 'hello, its me from A'
    a['a5'] = [[b, c], b, c]
    a['a6'] = True
    a['a7'] = False

    k = jsonparser.load('test_dictionary.json')
    assert a == k


def dictyamltest():
    a = dict()
    b = dict()
    c = dict()
    a['a1'] = 15
    a['a2'] = 15.99
    a['bruh'] = b
    a['a3'] = None
    a['a4'] = 'hello, its me from A'
    a['a6'] = True
    a['bleh'] = c
    a['good_job'] = list()
    a['a7'] = False
    a['a8'] = [18, -81.99, 'fffhhr', 'rhrhr\tjwdew']
    b['b6'] = 'tratatatata'

    k = yamlparser.load('test_dictionary.yaml')
    assert a == k


def dicttomltest():
    a = dict()
    b = dict()
    c = dict()
    a['a1'] = 15
    a['a2'] = 15.99
    a['a3'] = b
    a['a4'] = 'hello, its me from A'
    a['a5'] = [[15, 'hello'], [None, True], [-17, 299], False]
    a['a6'] = True
    a['a7'] = False
    b['b6'] = 'tratatatata'
    b['b7'] = c
    c['c1'] = 15
    c['c2'] = 'oraoraoraora'

    k = tomlparser.load('test_dictionary.toml')
    assert a == k


def serialize():
    temp = serializer.serialize_obj(fib)
    temp_2 = serializer.deserialize_obj(temp)

    assert temp_2(10) == fib(10)


recursive()
simple()
lambda_()
onemoretest()
dictyamltest()
dicttomltest()
dictjsontest()
serialize()
