for i in range(5, 12):
    print('Hello World!', i)
print()

for i in range(0, 10, 2):
    print('Hello World!', i)
print()

for i in range(10, 0, -1):
    print('Hello World!', i)
print()

for i in reversed(range(10)):
    print('Hello World!', i)
print()

count = int(input('반복할 횟수를 입력하세요: '))

for i in range(count):
    print('Hello World!', i)