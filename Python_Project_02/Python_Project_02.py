# Unit 08
kor, eng, math, sci = map(int, input().split())
print(kor >= 90 and eng > 80 and math > 85 and sci >= 80)

# Unit 09
s = '''\'Python\' is a \"programming language\" 
that lets you work quickly
and
integrate systems more effectively.'''
print(s)

# Unit 10
step = int(input())
a = tuple(range(-10, 9, step))
print(a)

# Unit 11
x=input().split()
del x[-1:-6:-1]
print(tuple(x))

s1=input()
s2=input()
print(s1[1::2], s2[::2], sep='')