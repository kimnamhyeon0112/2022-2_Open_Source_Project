def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b
    return mul_add
c = calc()
print(c(1),c(2),c(3),c(4),c(5))
print()

def calc():
    a = 3
    b = 5
    return lambda x: a * x + b
c = calc()
print(c(1),c(2),c(3),c(4),c(5))
print()

def calc():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total
        total = total + a * x + b
        print(total)
    return mul_add
c = calc()
c(1)
c(2)
c(3)
print()