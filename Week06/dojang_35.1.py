from pickletools import markobject


class Person:
    bag = []
    
    def put_bag(self, stuff):
        self.bag.append(stuff)
        
james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)
print()

class Person:
    def __init__(self):
        self.bag=[]
        
    def put_bag(self, stuff):
        self.bag.append(stuff)
        
james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)
print()