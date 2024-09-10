
"""
Bridge
- a structural design pattern that lets you split a large class into two separate hierarchies 
- abstraction and implementation - 
which can be developed independently of each

"""

import abc

class Shape(abc.ABC): # abstraction
    def __init__(self,color):
        self.color = color

    def show(self):
        pass


class Circle(Shape):
    def show(self):
        self.color.paint('Circle')
    

class Square(Shape):
    def show(self):
        self.color.paint('Square')


class Color(abc.ABC): # abstraction


    def paint(self,name):
        pass

class Blue(Color):
    def paint(self,name):
        print(f'this is blue {name}')

class Red(Color):
    def paint(self,name):
        print(f'this is red {name}')


blue = Blue()
circle = Circle(blue)
circle.show()


