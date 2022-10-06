def hello():
    print('hello world')
    hello()     # 자기자신을 호출(재귀호출)
    
hello()         # 최대 재귀 깊이가 1000이므로 1000번 실행하고 오류가 남

def hello(count):
    if count == 0:
        return
    
    print('Hello world',count)
    count -=1
    hello(count)
    
hello(5)