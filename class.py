class Person:
    def __init__(self, x=2, y=22):
        self.x=x
        self.y=y
        
        
    def disp(self):
        return self.x
p1 = Person()
print(p1.x)