import string
x=str(input())
a=[]
for i in x:
  a.append(i.translate(x.maketrans('','',string.punctuation)))
x=''.join(a)
x = x.split()
print(x.count('the'))