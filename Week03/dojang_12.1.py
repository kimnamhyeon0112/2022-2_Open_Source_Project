# 딕셔너리 만들기
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
print(lux)
print()

# key 이름 중복
lux = {'health': 490, 'health': 334, 'melee': 550, 'armor': 18.72}
print(lux)
print()

# 딕셔너리 key의 자료형
x = {'a': 3, '100': 100, False: 0}
print(x)
print()

# 빈 딕셔너리 만들기
x = {}
y = dict()
print(x)
print(y)
print()

# dict 키워드로 딕셔너리 만들기
a = dict(health =  490, mana =  334, melee =  550, armor = 18.72)
b = dict(zip(['health', 'mana', 'melee', 'armor'],[490, 334, 550, 18.72]))
c = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
d = dict({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})
print(a)
print(b)
print(c)
print(d)