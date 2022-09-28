a = [i for i in range(10)]
b = list(i for i in range(10))
c = [i + 5 for i in range(10)]
d = [i + 2 for i in range(10)]
print(a)
print(b)
print(c)
print(d)
print()

a = [i for i in range(10) if i % 2 == 0]
b = [i + 5 for i in range(10) if i % 2 == 1]
print(a)
print(b)
print()

a = [i * j for j in range(2, 10) for i in range(1, 10)]
print(a)