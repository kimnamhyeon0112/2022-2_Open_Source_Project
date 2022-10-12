import hello

print('main.py __name__:', __name__)
print()
# python Week06/hello.py를 터미널에 입력하고 실행하면
# hello 모듈 시작
# hello.py __name__: __main__
# hello 모듈 끝
# 처럼 출력이 바뀜

import calc

calc.add(50, 60)
calc.mul(50, 60)