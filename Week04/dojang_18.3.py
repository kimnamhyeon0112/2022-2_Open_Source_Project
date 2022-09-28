count = int(input('반복할 횟수를 입력하세요: '))

i = 0
while i < count:
    print(i)
    i += 1
print()

count2 = int(input('반복할 횟수를 입력하세요: '))

i = 0
for i in range(count + 1):
    if i % 2 == 0:
        continue
    print(i)