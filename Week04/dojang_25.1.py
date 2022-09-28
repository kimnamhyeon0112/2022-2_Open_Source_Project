x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('e')
print(x)
print()

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.update(a=90)
print(x)
print()

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.pop('a')
print(x)
print()

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.popitem()
print(x)
print()

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.clear()
print(x)
print()

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.get('a'))
print()

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.items())
print(x.keys())
print(x.values())
print()

keys = ['a', 'b', 'c', 'd']
x = dict.fromkeys(keys)
print(x)