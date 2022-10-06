a = {1,2,3,4}
b = a                   # a와 b는 하나의 set로 값을 공유
print(a is b, b)
b.add(5)                # 따라서 b에 값을 추가하면
print(a)                # a= {1,2,3,4,5}
print(b)                # b= {1,2,3,4,5}
b = a.copy()            # 그러나 a를 copy하면 b와 a는 다른 세트
print(a is b, a == b)   # 따라서 a와 b가 같은지 비교하면 False이지만 값은 같으므로 True
print()

a = {1,2,3,4}
b = a.copy()            # b는 a를 copy했으므로 둘은 서로 다른 set
b.add(5)                # 따라서 b에 값을 추가해도
print(a)                # a= {1,2,3,4}
print(b)                # b= {1,2,3,4,5}