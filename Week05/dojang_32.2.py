a = [1,2,3,4,5]
b = [2,4,6,8,10]
print(list(map(lambda x,y: x * y, a,b)))        # 람다식에 map 사용

a = [8,3,2,10,15,7,1,9,0,11]
print(list(filter(lambda x: x>5 and x <10, a))) # 람다식에 filter 사용, filter란 조건에 맞는 요소만 가져옴

a = [1,2,3,4,5]
from functools import reduce
print(reduce(lambda x, y: x+y, a))              # 람다식에 reduce 사용, reduce란 지정된 함수로 요소를 처리