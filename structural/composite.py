"""
Composite
- a structural design pattern that lets you compose 
objects into tree structures and then work 
with these structures as if they were individual objects.

"""

import abc

class Being(abc.ABC): # abstract component 
    def add(self,child):
        pass
    def remove(self,child):
        pass

    def composite(self,child ):
        pass

    @abc.abstractmethod
    def execute(self):
        pass


class Human(Being): # concrete composite
    def __init__(self) -> None:
        self._children = []

    def add(self,child):
        self._children.append(child)

    def remove(self,child):
        self._children.remove(child)


    def is_composite(self):
        return True
        

    def execute(self):
        print("this is a human")
        for child in self._children:
            child.execute()


class Male(Human): # leaf
    def __init__(self,name) -> None:
        self.name = name

    def is_composite(self):
        return False
    
    def execute(self):
        print(f'\t Male {self.name}')
    


class FeMale(Human): # leaf
    def __init__(self,name) -> None:
        self.name = name

    def is_composite(self):
        return False
    
    def execute(self):
        print(f'\t FeMale {self.name}')



def client_composite():
    f1 = FeMale('jane')
    f2 = Male('katty')
    m1 = Male('mike')

    h1 = Human()
    h1.add(f1)
    h1.add(f2)
    h1.add(m1)

    h1.execute()

client_composite()