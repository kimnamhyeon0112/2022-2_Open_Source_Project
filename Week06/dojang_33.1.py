x = 10
def foo():
    print(x)
foo()
print(x)
print()

x = 10
def foo():
    x = 20
    print(x)
foo()
print(x)
print()

x = 10
def foo():
    global x
    x = 20
    print(x)
foo()
print(x)
print()

def foo():
    global x
    x = 20
    print(x)
foo()
print(x)