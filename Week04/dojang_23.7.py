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