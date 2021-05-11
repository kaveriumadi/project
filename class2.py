from builtins import staticmethod
class Person:
    cnt=0
    def __init__(self, name, age, gender='Male', country='India'):
        self.x=name
        self.y=age
        self.g=gender
        self.c=country
        Person.cnt=Person.cnt+1
        
    def display(self):
        print("person object details are:")
        print('Name:',self.x)
        print('Age:',self.y)
        print('gender:', self.g)
        
    @staticmethod
    def obj_count():
        print("object count:", Person.cnt)
        
    @classmethod
    def object_cnt(cls):
        print("object details:",Person.cnt)
        
        
p1 = Person("ravi", 22, "male", "india")
print(p1.x,p1.y)

Person.obj_count()
Person.object_cnt()

print(p1.display())