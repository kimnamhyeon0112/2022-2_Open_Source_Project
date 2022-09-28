a = [10,20,30]
a.append(500)
print(a)
print(len(a))
print()

a = []
a.append(10)
print(a)
print()

a = [10,20,30]
a.append([500,600])
print(a)
print(len(a))
print()

a = [10,20,30]
a.extend([500,600])
print(a)
print(len(a))
print()

a = [10,20,30]
a.insert(2, 500)
print(a)
print(len(a))
print()

a = [10,20,30]
a.insert(0, 500)
print(a)
print(len(a))
print()

a = [10,20,30]
a.insert(len(a), 500)
print(a)
print(len(a))
print()

a = [10,20,30]
a.insert(1, [500,600])
print(a)
print(len(a))
print()

a = [10,20,30]
a[1:1] = [500, 600]
print(a)
print(len(a))
print()

a = [10,20,30]
a.pop()
print(a)
print(len(a))
print()

a = [10,20,30]
a.pop(1)
print(a)
print(len(a))
print()

a = [10,20,30]
del a[1]
print(a)
print(len(a))
print()

a = [10,20,30]
a.remove(20)
print(a)
print(len(a))
print()

a = [10,20,30,20]
a.remove(20)
print(a)
print(len(a))
print()

a = [10,20,30,15,20,40]
print(a.index(20))
print()

a = [10,20,30,15,20,40]
print(a.count(20))
print()

a = [10,20,30,15,20,40]
print(a.reverse())
print()

a = [10,20,30,15,20,40]
print(a.sort())
print()

a = [10,20,30]
print(a.clear())
print()

a = [10,20,30]
del a[:]
print(a)
print()

a = [10,20,30]
a[len(a):] =[500]
print(a)
print()

a = [10,20,30]
a[len(a):] =[500, 600]
print(a)
print()