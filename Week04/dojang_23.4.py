a = [[10, 20], [30, 40]]
b = a
b[0][0] = 500
print(a)
print(b)
print()

a = [[10, 20], [30, 40]]
b = a.copy()
b[0][0] = 500
print(a)
print(b)
print()

a = [[10, 20], [30, 40]]
import copy             # copy 모듈을 가져옴
b = copy.deepcopy(a)    # copy.deepcopy 함수를 사용하여 깊은 복사
b[0][0] = 500
print(a)
print(b)