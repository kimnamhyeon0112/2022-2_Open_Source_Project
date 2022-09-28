a = [38,21,53,62,19]
smallest = a[0]
largest = a[0]
for i in a:
    if i < smallest:
        smallest = i
print(smallest)
for i in a:
    if i > largest:
        largest = i
print(largest)
print()

a = [38,21,53,62,19]
a.sort()
print(a[0])
a.sort(reverse=True)
print(a[0])
print()

a = [38,21,53,62,19]
print(min(a))
print(max(a))
print()

a = [10,10,10,10,10]
x = 0
for i in a:
    x += i
print(x)
print()

a = [10,10,10,10,10]
print(sum(a))