a = [0,0,0,0,0]
b = a
print(b)
print(a is b)
b[2] = 99
print(a, b, end='\n')
print()

a = [0,0,0,0,0]
b = a.copy()
print(b)
print(a is b, a == b)
b[2] = 99
print(a, b, end='\n')