# Unit 16
num = int(input())

for i in range(1, 10):
    print(num, i, sep= ' * ', end= ' = ')
    print(num * i)
    
# Unit 17
my_money = int(input())

while my_money >= 1350:
    my_money -= 1350
    print(my_money)
    
# Unit 18
start, stop = map(int,input().split())

i = start

while True:
    if i > stop:
        break
    if i % 10 == 3:
        i += 1
        continue
    print(i, end = ' ')
    i+=1
    
# Unit 19
a = int(input())
for i in range(a):
  for j in range(a-i-1):
    print(' ',end='')
  for j in range(2*i+1):
    print('*',end='')
  print()