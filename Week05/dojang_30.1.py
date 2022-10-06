def print_nums(a,b,c):
    print(a)
    print(b)
    print(c)

x = [10,20,30]
print_nums(*x)

def print_numbers(*args):       # 인수를 넣지 않았을 때 args를 씀
     for arg in args:
         print(arg)
print_numbers(10)