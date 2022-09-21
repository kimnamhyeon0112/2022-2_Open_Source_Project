# 딕셔너리 키에 접근
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
print(lux['health'])
print()

# 딕셔너리 키에 값 할당
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux['health'] = 2000
print(lux)
print()

# 딕셔너리 키 존재 여부 확인
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
print('health' in lux)
print('attack' in lux)
print()

# 딕셔너리 키 개수 구하기
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
print(len(lux))
print(len({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}))