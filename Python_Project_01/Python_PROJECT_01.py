#Unit 03
print('Hello, world!')
print('Hello, world!')

#Unit 05
print(102*0.6+225)

#unit 06
a = 50
b = 100
c = None
print(a, b, c)

language, english, math, science = map(int, input().split())
avg = int((language + english + math + science) / 4)
print(avg)

#Unit 07
year, month, day, hour, minute, second = input().split()
print(year, month, day, sep="-", end="T")
print(hour, minute, second, sep=":")
    