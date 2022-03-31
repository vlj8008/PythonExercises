

from abc import ABC, abstractmethod #ABC stands for Abstract Base Classes

#Shape Class
class Shape(ABC): # inherit ABC module in to the Shape class
#method 1
    @abstractmethod #adding decorator makes this method abstract. Must implement in sub-class
    def area(self): pass
#method 2
    @abstractmethod#adding decorator makes this method abstract. Must implement in sub-class
    def perimeter(self): pass

#method 3

    def farewell(self): #regular method (no decorator)
        return("Have a nice day!")


#Shape is a sub-class of Shape and is inheriting from Shape
class Square(Shape):
    def __init__(self, side):
        self.__side = side
#method 1 from Parent
    def area(self): #have to provide implementation details because area method from parent is abstract
        return self.__side * self.__side
#method 2 from Parent
    def perimeter(self): #have to provide implementation details because area method from parent is abstract
        return self.__side * self.__side
#method 3 (not from parent)
    def defining(self):
        return("I am a square")




#shape = Shape() #Can't instantiate shape as it is an abstract class.

square = Square(5) #instantiating sqare object
print (square.area())
print(square.perimeter())
print(square.farewell()) #calling the farewell method from the parent class
print(square.defining()) #calling own method from own class (not from parent class)



