try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:                           # 에러발생
    print('숫자를 0으로 나눌 수 없습니다')
else:                                               # 예외 없음
    print(y)
finally:                                            # 에러 여부 상관없이 실행
    print('코드 실행이 끝났습니다')
    