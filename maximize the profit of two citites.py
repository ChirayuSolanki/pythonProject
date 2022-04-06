ccesing class constructorin the sub class
class Square :
    def __init__(self,x):
        self.x = x
    def area(self):
        print("Area : ",self.x*self.x)
        

class Rectangle :
    def __init__(self,x,y):
         super().__init__(x)
        self.y = y
    def area(self):
        super().area()
        print("Area of rectangle : ",self.x*self.y)

a = 5
b = 6
a =Rectangle(a,b)
a.area()











