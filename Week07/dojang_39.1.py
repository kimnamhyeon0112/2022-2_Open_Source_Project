print(dir([1,2,3]))     # dir: 객체의 메서드 확인
print()

print([1,2,3].__iter__)     # __iter__: list의 이터레이터
print()

it = [1,2,3].__iter__()
print(it.__next__())
print(it.__next__())
print(it.__next__())
# print(it.__next__())        # list의 크기가 3이므로 이 줄부터 에러
print()

print('Hello, World!'.__iter__())       # str iterator
print({'1': 1, '2': 2}.__iter__())      # dict iterator
print({1,2,3}.__iter__())               # set iterator
print()

it = range(3).__iter__()
for i in range(3):
    print(it.__next__())