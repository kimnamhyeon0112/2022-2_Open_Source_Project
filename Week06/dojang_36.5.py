class Person:
    def greetings(self):
        print('안녕하세요')

class University:
    def manage_credit(self):
        print('학점 관리')

class Undergraduate(Person, University):
    def study(self):
        print('공부하기')

james = Undergraduate()
james.greetings()
james.manage_credit()
james.study()
print()

class A:
    def greetings(self):
        print('안녕하세요 A입니다')
        
class B(A):
    def greetings(self):
        print('안녕하세요 B입니다')
        
class C(A):
    def greetings(self):
        print('안녕하세요 C입니다')
        
class D(B, C):
    pass

james = D()
james.greetings()
print(D.mro())