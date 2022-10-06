a = {1,2,3,4}
a.add(5)    # 요소 추가
print(a)

a.remove(3) # 요소 삭제, 없으면 Error
print(a)

a.discard(2) # 요소 삭제, 없으면 통과
print(a)

a.discard(3)
print(a)
print()

a = {1,2,3,4}
a.pop()
print(a)

a.clear()
print(a)

b = {'hello':1500}      # 딕셔너리, set모두 같은 {}를 사용하지만 딕셔너리는 키: 값이 존재하고
c =  {1}                # set는 값만 존재
print(type(b), type(c))