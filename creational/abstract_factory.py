"""
Abstract Factory
- Abstract Factory Pattern serves to provide 
    an interface for creating related/dependent 
    objects without need to specify their actual class

Car => Benz, Bmw => Suv, Coupe
benz suv = gla
bmw suv => x1
benz coupe => cls bmw coupe =>m2
"""

from abc import ABC, abstractmethod


class Car(ABC): # Abstract Factory
    @abstractmethod
    def call_suv(self):
        pass

    @abstractmethod
    def call_coupe(self):
        pass


class Benz(Car): # Concrete Factory 1
    def call_suv(self):
        return Gla()

    def call_coupe(self):
        return Cls()


class Bmw(Car): # Concrete Factory 2
    def call_suv(self):
        return X1()

    def call_coupe(self):
        return M2()


class Suv(ABC): # Abstract Product 1
    @abstractmethod
    def create_suv(self):
        pass


class Coupe(ABC): # Abstract Product 2
    @abstractmethod
    def create_coupe(self):
        pass


class Gla(Suv): # Product 1-1
    def create_suv(self):
        print(f" Benz + suv => Gla") 


class X1(Suv): # Product 2-1
    def create_suv(self):
        print(f" Bmw + suv => X1") 


class M2(Coupe): # Product 2-2
    def create_coupe(self):
        print(f" Bmw + coupe => M2") 


class Cls(Coupe):# Product 1-2
    def create_coupe(self):
        print(f" Benz + coupe => Cls") 


def client_suv(order): #client
    brand = {"bmw": Bmw, "benz": Benz}
    result = brand[order]().call_suv()
    result.create_suv()

def client_coupe(order):#client
    brand = {"bmw": Bmw, "benz": Benz}
    result = brand[order]().call_coupe()
    result.create_coupe()

client_coupe('benz')