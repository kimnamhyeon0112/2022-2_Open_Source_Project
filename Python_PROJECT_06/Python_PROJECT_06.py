# Unit 25
keys = input().split()
values = map(int,input().split())

x = dict(zip(keys, values))
x.pop('delta')
x = {key: value for key, value in x.items() if value != 30}

# Unit 26
x, y = map(int, input().split())
a = {i for i in range(1, x+1) if x % i == 0}
b = {i for i in range(1, y+1) if y % i == 0}

divisor = a & b
result = 0
if type(divisor) == set:
    result = sum(divisor)
print(result)

# Unit 27
with open('words.txt', 'r') as file:
  text = file.readline()
  words = text.split()
  for word in words:
    if 'c' in word:
      print(word.strip(',.'))
      
# Unit 28
with open("words2.txt","r") as file:
    word = None
    while word != '':
        word = file.readline().strip('\n')
        if word == word[::-1]:
            print(word)