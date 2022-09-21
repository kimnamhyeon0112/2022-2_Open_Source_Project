# 인덱스 사용하기
a = [38, 21, 53, 62, 19]
b = (38, 21, 53, 62, 19)
r = range(0, 10, 2)
hello = 'Hello World!'
print(a[0], a[2], a[4])
print(b[0])
print(r[2])
print(hello[7])
print()

# 음수 인덱스 지정
a = [38, 21, 53, 62, 19]
b = (38, 21, 53, 62, 19)
r = range(0, 10, 2)
hello = 'Hello World!'
print(a[-1], a[-5])
print(b[-1])
print(r[-3])
print(hello[-4])
print()

# 잘못된 인덱스 범위
a = [38, 21, 53, 62, 19]
print(a[5])
print()

# 마지막 요소에 접근
a = [38, 21, 53, 62, 19]
print(len(a))
print(a[5], a[4], a[len(a)], a[len(a) - 1])
print()

# 요소에 값 할당
a = [0, 0, 0, 0, 0]
a[0] = 38
a[1] = 21
a[2] = 53
a[3] = 62
a[4] = 19
a[5] = 90
print(a)
print(a[0])
print(a[4])
print()

# del로 요소 삭제
a = [38, 21, 53, 62, 19]
b = (38, 21, 53, 62, 19)
del a[2]
del b[2]
print(a)
print(b)