x = 20
if x == 10:
      print('10입니다.')
elif x == 20:
      print('20입니다.')
print()

x = 30
 
if x == 10:             # x가 10일 때
    print('10입니다.')
elif x == 20:           # x가 20일 때
    print('20입니다.')
else:                   # 앞의 조건식에 모두 만족하지 않을 때
    print('10도 20도 아닙니다.')
print()

if x == 10:
    print('10입니다.')
else:
    print('10도 20도 아닙니다.')
# elif x == 20:    # elif 앞에 else가 오면 잘못된 문법
#    print('20입니다.')
print()

button = int(input())
 
if button == 1:
    print('콜라')
elif button == 2:
    print('사이다')
elif button == 3:
    print('환타')
else:
    print('제공하지 않는 메뉴')
print()