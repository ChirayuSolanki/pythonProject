# a python program to claculate square,square root,cube of three different object using abstract classes
from abc import ABC,abstractmethod
class Myclass(ABC):
    @abstractmethod
    def calculate(self,x):
        pass

class Sub1(Myclass):
    def calculate(self,x):
        print("Square is = ",x*x)

import math
class Sub2(Myclass):
    def calculate(self, x):
        print("Square root is = ", math.sqrt(x))


class Sub3(Myclass):
    def calculate(self, x):
        print("Square is = ", x**3)

obj1 = Sub1()
obj1.calculate(9)
obj2 = Sub2()
obj2.calculate(9)
obj3 = Sub3()
obj3.calculate(9)



