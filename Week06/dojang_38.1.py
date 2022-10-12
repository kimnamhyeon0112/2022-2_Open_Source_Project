def ten_div(x):
    return 10/x

print(ten_div(10))
print()

try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10/x
    print(y)
except:
    print('예외가 발생했습니다')
print()

y = [10, 20, 30]
try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    print(y[index] / x)
except ZeroDivisionError:                                   # 숫자를 0으로 나눈경우 에러
    print('숫자를 0으로 나눌 수 없습니다')
except IndexError:                                          # y의 인덱스 0~2사이 숫자가 아닌경우 에러
    print('잘못된 인덱스입니다')
print()

y = [10, 20, 30]
try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    print(y[index] / x)
except ZeroDivisionError as e:                                   # 숫자를 0으로 나눈경우 에러
    print('숫자를 0으로 나눌 수 없습니다', e)                       # zeroDivisionError의 에러메시지 -> division by zero 
except IndexError as e:                                          # y의 인덱스 0~2사이 숫자가 아닌경우 에러
    print('잘못된 인덱스입니다', e)                                 # IndexError의 에러메시지 -> list index out of range
print()
