class Person:
    def greetings(self):
        print('안녕하세요')

class Student(Person):
    def study(self):
        print('공부하기')
        
james = Student()
james.greetings()
james.study()