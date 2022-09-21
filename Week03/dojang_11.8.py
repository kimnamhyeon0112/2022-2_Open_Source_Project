x=input().split()
del x[-1:-6:-1]
print(tuple(x))