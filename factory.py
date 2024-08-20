"""
Factory
- Factory is a creational design pattern that provides an interface for creating objects 
    in a superclass, but allows subclasses to alter the type of objects that will be created.

 component = 1. creator, 2. product, 3.client
"""

from abc import ABC, abstractmethod


class File(ABC):  # product
    def __init__(self, file) -> None:
        self.file = file

    @abstractmethod
    def make(self):
        pass

    def call_edit(self):
        product = self.make()
        result = product.edit(self.file)
        return result


class XmlMake(File):  # product
    def make(self):
        return Xml()


class PdfMake(File):  # product
    def make(self):
        return Pdf()


class Xml:  # creator
    def edit(self, file):
        return f"working on {file} Xml..."


class Pdf:  # creator
    def edit(self, file):
        return f"working on {file} pdf..."


def client(file,format):
    formats = {'pdf' : PdfMake,'xml' : XmlMake}
    result = formats[format](file)
    return result.call_edit()



print(client('iran','pdf'))
