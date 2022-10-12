from tkinter import Y


def print_hello():
    hello = 'Hello, world'
    def print_message():
        print(hello)
    print_message()
print_hello()
print()

def A():
    x = 10
    def B():
        x = 20
    B()
    print(x)
A()
print()

def A():
    x = 10
    def B():
        nonlocal x
        x = 20
    B()
    print(x)
A()
print()

def A():
    x = 10
    y = 100
    def B():
        x = 20
        def C():
            nonlocal x
            nonlocal y
            x = x + 30
            y = y + 300
            print(x)
            print(y)
        C()
    B()
A()
print()

x = 1
def A():
    x = 10
    def B():
        x = 20
        def C():
            global x
            x = x+30
            print(x)
        C()
    B()
A()