from factory.parsers import serializer, jsonparser

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
a['a8'] = 'hello, its me from A'
a['a9'] = 15.99
a['a10'] = 15
a['a11'] = None

jsonparser.dump(a, 'tests/test_dictionary.json')
k = jsonparser.load('tests/test_dictionary.json')

print(a == k)
