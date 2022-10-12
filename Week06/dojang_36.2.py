class Person:
    def greetings(self):
        print('안녕하세요')

class Student(Person):
    def __init__(self):
        self.person_list = []
        
    def append_person(self, person):
        self.person_list.append(person)
print()