import enum


a = [38,21,53,62,19]
for i in a:
    print(i)
for i in [38,21,53,62,19]:
    print(i)
print()

a = [38,21,53,62,19]
for index, value in enumerate(a):
    print(index, value)
for index, value in enumerate(a):
    print(index + 1, value)
for index, value in enumerate(a, start=1):
    print(index, value)
print()

a = [38,21,53,62,19]
i = 0
while i < len(a):
    print(a[i])
    i += 1
print()

a = [38,21,53,62,19]
i = 0
while i <= len(a):
    print(a[i])
    i += 1