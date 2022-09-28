a = int(input())
for i in range(a):
  for j in range(a-i-1):
    print(' ',end='')
  for j in range(2*i+1):
    print('*',end='')
  print()
  
# 다른 방법
# 왼쪽 출력
for i in range(height):
    for j in reversed(range(height)):
        if j > i:
            print(' ', end='')
        else:
            print('*', end='')
            
# 오른쪽 출력
for i in range(height):
  for j in reversed(range(height)):
    if j < i:
      print('*', end='')
  print()
  
# 최종 코드
height = int(input())
for i in range(height):
  for j in reversed(range(height)):
    if j > i:
      print(' ', end='')
    else:
      print('*', end='')
    if j < i:
      print('*', end='')
  print()