keys = ['a', 'b', 'c', 'd']
x = {key: value for key, value in dict.fromkeys(keys).items()}
print(x)
print()

print({key: 0 for key in dict.fromkeys(['a', 'b', 'c', 'd']).keys()})               # 키만 가져옴
print({value: 0 for value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.values()})        # 값을 키로 사용
print()

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
 
for key, value in x.items():
    if value == 20:    # 값이 20이면
        del x[key]     # 키-값 쌍 삭제
 
print(x)
print()

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x = {key: value for key, value in x.items() if value != 20}
print(x)