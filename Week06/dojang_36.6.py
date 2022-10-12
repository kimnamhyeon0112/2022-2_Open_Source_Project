from abc import *           # Abstract Base Class의 모든 함수 호출

class StudentBase(metaclass = ABCMeta):
    @abstractmethod
    def study(self):
        pass
    
    @abstractmethod
    def go_to_school(self):
        pass
    
class Student(StudentBase):
    def study(self):
        print('공부하기')
        
    def go_to_school(self):
        print('학교가기')

james = Student()
james.study()
james.go_to_school()