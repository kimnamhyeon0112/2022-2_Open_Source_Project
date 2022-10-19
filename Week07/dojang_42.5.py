class Trace:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        r = self.func(*args, **kwargs)
        
        print('{0}(args = {1}, kwargs = {2}) -> {3}'.format(self.func.__name__, args, kwargs, r))
        return r
@Trace
def add(a, b):
    return a + b

print(add(10, 20))
print(add(a=10, b=20))
print()

class IsMultiple:
    def __init__(self, x):
        self.x = x
        
    def __call__(self, func):
        def wrapper(a, b):
            r = func(a, b)
            if r % self.x == 0:
                print('{0}의 반환값은 {1}의 배수입니다'.format(func.__name__, self.x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아닙니다'.format(func.__name__, self.x))
            return r
        return wrapper

@IsMultiple(3)                  # def __init__(self, x):    self.x = x때문에 데코레이터에 인수를 입력해야함
def add(a, b):
    return a + b
print(add(10 ,20))
print(add(2, 5))