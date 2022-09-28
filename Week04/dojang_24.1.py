print('Hello, world!'.replace('world', 'Python'))
print()

s = 'Hello, world!'
s = s.replace('world!', 'Python')
print(s)
print()

table = str.maketrans('aeiou', '12345')
print('apple'.translate(table))
print()

print('apple pear grape pineapple orange'.split())
print()

print('apple, pear, grape, pineapple, orange'.split(', '))
print()

print(' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))
print()

print('-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))
print()

print('python'.upper())
print('python'.lower())
print()

print('   Python   '.lstrip())
print('   Python   '.rstrip())
print('   Python   '.strip())
print()

print(',   Python.   '.lstrip(',.'))
print(',   Python.   '.rstrip(',.'))
print(',   Python.   '.strip(',.'))
print()

print('python'.ljust(10))
print('python'.rjust(10))
print('python'.center(10))
print('python'.center(11))
print()

print('python'.rjust(10).upper())
print()

print('35'.zfill(4))        # 숫자 앞에 0을 채움
print('3.5'.zfill(6))       # 숫자 앞에 0을 채움
print('hello'.zfill(10))    # 문자열 앞에 0을 채울 수도 있음
print()

print('apple pineapple'.find('pl'))
print('apple pineapple'.find('xy'))
print('apple pineapple'.rfind('pl'))
print('apple pineapple'.rfind('xy'))
print('apple pineapple'.index('pl'))
print()

print('apple pineapple'.rindex('pl'))
print()

print('apple pineapple'.count('pl'))
print()