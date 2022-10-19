it = iter(range(3))
print(next(it))
print(next(it))
print(next(it))
print()

import random
it = iter(lambda : random.randint(0, 5), 2)             # 난수 생성하다가 2나오면 종료
print(next(it))
print(next(it))
print()

import random
for i in iter(lambda : random.randint(0, 5), 2):        # 난수 생성하다가 2나오면 종료
    print(i, end=' ')
print()

import random

while True:
    i = random.randint(0, 5)        # 난수 생성하다가 2나오면 종료
    if i == 2:
        break
    print(i, end=' ')
print()

it = iter(range(3))
print(next(it, 10))
print(next(it, 10))
print(next(it, 10))
print(next(it, 10))
print(next(it, 10))