"""
Template method 
     a behavioral design pattern that defines the skleton of algorithem in the superclass
    but let subclasses oveerwrite specific step of the algorithme with out changing its structure

"""

import abc


class Top(abc.ABC):
    def template(self):
        self.first_common()
        self.second_common()
        self.third_requier()
        self.fourth_requier()

    def first_common(self):
        print('first common')

    def second_common(self):
        print('second common')

    @abc.abstractmethod
    def third_requier(self):
        pass

    @abc.abstractmethod
    def fourth_requier(self):
        pass


class One(Top):
    def third_requier(self):
         print(" third one ")
    
    def fourth_requier(self):
        print("fourth one ")
    


class Two(Top):
    def third_requier(self):
        print("third two")
    
    def fourth_requier(self):
        print("fourth two ")
    

def client(kls):
    kls.template()


client(Two())

