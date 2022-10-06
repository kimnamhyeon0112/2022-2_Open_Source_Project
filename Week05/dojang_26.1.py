fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print(fruits)   # 세트는 요소에 순서가 없기 때문에 순서는 무작위로 출력됨
print()

fruits = {'orange', 'orange', 'cherry'}
print(fruits)   # 세트의 요소는 중복이 불가하기때문에 orange와 cherry만 출력됨
print()

fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print('strawberry' in fruits)
print('apple' in fruits)
print('peach' not in fruits)
print('orange' not in fruits)
print()

a = set('apple')    # 중복 요소인 p는 1번만 출력
b = set(range(5))
c = set()
print(a, b, c)
print(type(a), type(b), type(c))