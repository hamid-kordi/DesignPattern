"""
Prototype
-   Prototype is a creational design pattern that 
    lets you copy existing 
    objects without making your code dependent on their

"""

import copy


class Prototype:
    def __init__(self) -> None:
        self._object = {}

    def register(self, name, obj):
        self._object[name] = obj

    def unregister(self, name):
        del self._object[name]

    def clone(self, name, **kwargs):
        cloned_object = copy.deepcopy(self._object.get(name))
        cloned_object.__dict__.update(kwargs)
        return cloned_object


def client_portotype(name, obj, **kwargs):
    prototype = Prototype()
    prototype.register(name, obj)
    return prototype.clone(name, **kwargs)


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


p = Person(name="iran", age=34)


p_cloned = client_portotype("p11", p)
