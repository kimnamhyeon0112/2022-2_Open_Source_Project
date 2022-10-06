# Unit 20
a, b = map(int, input().split())

for i in range(a, b + 1):
    if i % 5 == 0 and i % 7 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Fizz")
    elif i % 7 == 0:
        print("Buzz")
    else:
        print(i)
        
# Unit 22
start, stop = map(int, input().split())
a = [2 ** i for i in range(start, stop + 1)]
del a[1]
del a[-2]
print(a)

# Unit 23
col, row = map(int, input().split())
matrix = []
for i in range(row):
  matrix.append(list(input()))
output = []
for i in range(len(matrix)):
    output.append([])
    for j in range(len(matrix[i])):
      this = matrix[i][j]
      if this == '*':
        output[i].append(this)
        continue
      else:
        data = 0
        if j < len(matrix[i])-1 and matrix[i][j+1] == '*':
          data += 1
        if j != 0 and matrix[i][j-1] == '*':
          data += 1
        if i < len(matrix)-1 and j < len(matrix[i])-1 and matrix[i+1][j+1] == '*':
          data += 1
        if i < len(matrix)-1 and matrix[i+1][j] == '*':
          data += 1
        if j != 0 and i < len(matrix)-1 and matrix[i+1][j-1] == '*':
          data += 1
        if i != 0 and j < len(matrix[i])-1 and matrix[i-1][j+1] == '*':
          data += 1
        if i != 0 and matrix[i-1][j] == '*':
          data += 1
        if i != 0 and j != 0 and matrix[i-1][j-1] == '*':
          data += 1
        output[i].append(data)

for i in range(len(output)):
  for j in range(len(output[i])):
    print(output[i][j], end='')
  print()
  
# Unit 24
import string
x=str(input())
a=[]
for i in x:
  a.append(i.translate(x.maketrans('','',string.punctuation)))
x=''.join(a)
x = x.split()
print(x.count('the'))

a = list(map(int,input().split(';')))
a.sort(reverse=True)
for price in a:
    print('{:>9,}'.format(price))