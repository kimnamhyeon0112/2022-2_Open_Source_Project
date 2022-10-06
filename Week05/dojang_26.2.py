a = {1,2,3,4}
b = {3,4,5,6}
print(a|b)  # or연산
print(a&b, set.intersection(a, b))  # setintersection: 교집합
print(a-b, set.difference(a, b))    # difference: 차집합   
print(a^b, set.symmetric_difference(a, b))  # ^ or symmetric_difference: 대칭 차집합
print(set.union(a, b))  # union: 합집합(A U B)
print()

a = {1,2,3,4}
a |= {5}        # 요소 추가
a.update({6})   # 요소 추가
print(a)
print()

a = {1,2,3,4}
a &= {0,1,2,3,4}                    # 겹치는 요소만 저장
a.intersection_update({0,1,2,3,4})  # 겹치는 요소만 저장
print(a)
print()

a = {1,2,3,4}
a -= {3}                    # 요소 제거
print(a)
a.difference_update({2})    # 요소 제거
print(a)
print()

a = {1,2,3,4}
a ^= {3,4,5,6}                          # 교집합 제거
print(a)
a.symmetric_difference_update({1,2})    # 교집합 제거
print(a)
print()

a = {1,2,3,4}
print(a <= {1,2,3,4}, a.issubset({1,2,3,4,5}))
print(a < {1,2,3,4,5})
print(a >= {1,2,3,4}, a.issuperset({1,2,3,4}))
print(a > {1,2,3})
print(a == {1,2,3,4}, a == {4,2,1,3}, a != {1,2,3})
print(a.isdisjoint({5,6,7,8}))      # 겹치는 요소 유무 확인, 없으면 True 있으면 False