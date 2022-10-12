import square2                  # square2.py import

print(square2.base)             # square2의 base변수 사용
print(square2.square(10))       # square2의 square함수 사용
print()

from square2 import base, square    # square2.py에서(from) base와 square 사용(import)
print(base)
print(square(10))
print()

import person

maria = person.Person('마리아', 20, '서울시 서초구 반포동')
maria.greetings()
print()

from person import Person

maria = Person('마리아', 20, '서울시 서초구 반포동')
maria.greetings()