import math                     # math모듈 가져오기
print(math.pi)
print(math.sqrt(4.0))
print(math.sqrt(2.0))
print()

import math as m            # math 모듈을 가져와 이름을 m으로 지정
print(m.sqrt(4.0))
print(m.sqrt(2.0))
print()

from math import pi         # math 모듈의 pi만 가져오기
print(pi)
print()

from math import sqrt       # math 모듈의 sqrt만 가져오기
print(sqrt(4.0))
print(sqrt(2.0))
print()

from math import pi, sqrt       # math 모듈의 pi, sqrt만 가져오기
print(pi)
print(sqrt(4.0))
print(sqrt(2.0))
print()

from math import *       # math 모듈의 모든 변수, 함수, 클래스 가져오기
print(sqrt(4.0))
print(sqrt(2.0))
print()

from math import sqrt as s      # math 모듈의 sqrt를 가져와 이름을 s로 지정
print(s(4.0))
print(s(2.0))
print()

from math import sqrt as s, pi as p      # math 모듈의 sqrt를 가져와 이름을 s로 지정
print(s(4.0))
print(s(2.0))
print(p)