class Person:
    def greetings(self):
        print('안녕하세요')

class Student(Person):
    def greetings(self):
        print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다')

james = Student()
james.greetings()
print()

class Person:
    def greetings(self):
        print('안녕하세요')

class Student(Person):
    def greetings(self):
        super().greetings()     # 기반 클래스의 메서드 호출하여 중복 줄임
        print('저는 파이썬 코딩도장 학생입니다.')
        
james = Student()
james.greetings()
