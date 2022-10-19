def hello():
    print('hello 시작')
    print('hello')
    print('hello 끝')
    
def world():
    print('world 시작')
    print('world')
    print('world 끝')
    
hello() ; world()
print()

def trace(func):
    def wrapper():
        print(func.__name__, '시작')
        func()
        print(func.__name__, '끝')
    return wrapper

def hello():
    print('hello')
    
def world():
    print('world')
    
trace_hello = trace(hello)
trace_world = trace(world)
trace_hello() ; trace_world()
print()

def trace(func):
    def wrapper():
        print(func.__name__, '시작')
        func()
        print(func.__name__, '끝')
    return wrapper

@trace                      # @데코레이터를 사용함으로써 trace(func)에서 hello(), world()를 @trace로 묶었으므로 hello(), world() 호출 가능
def hello():
    print('hello')
    
@trace
def world():
    print('world')
    
hello() ; world()