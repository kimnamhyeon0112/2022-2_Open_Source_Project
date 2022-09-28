a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)):
    a[i] = int(a[i])
print(a)
print()

a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))
print(a)
print()

a = list(map(str, range(10)))
print(a)
print()

a = input().split()
print(a)
print()

a = map(int, input().split())
print(a)
print(list(a))
print()

a, b = [10, 20]
print(a)
print(b)
print()

x = input().split()    # input().split()의 결과는 문자열 리스트
m = map(int, x)        # 리스트의 요소를 int로 변환, 결과는 맵 객체
print(a, b = m)               # 맵 객체는 변수 여러 개에 저장할 수 있음