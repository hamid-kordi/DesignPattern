"""
builder
- Builder is a creational design pattern that lets you 
    construct complex objects step by step.
    The pattern allows you to produce different 
    types and representations of an object using the same construction code.

"""

from abc import ABC, abstractmethod


class Car:
    def __init__(self) -> None:
        self._wheel = None
        self._engine = None
        self._body = None

    def set_wheel(self, wheel):
        self._wheel = wheel

    def set_engine(self, engine):
        self._engine = engine

    def set_body(self, body):
        self._body = body

    def detail(self):
        print(f"boy is {self._body.shape}")
        print(f"enigne is {self._engine.power}")
        print(f"wheel is {self._wheel.size}")


class Body:
    shape = None
    ...


class Engine:
    power = None
    ...


class Wheel:
    size = None
    ...


class Abstractbuilder(ABC):
    @abstractmethod
    def get_wheel(self):
        pass

    @abstractmethod
    def get_engine(self):
        pass

    @abstractmethod
    def get_body(self):
        pass


class Benz(Abstractbuilder):
    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 20
        return wheel

    def get_body(self):
        body = Body()
        body.shape = "sedan"
        return body

    def get_engine(self):
        engine = Engine()
        engine.power = 300
        return engine


class Bmw(Abstractbuilder):
    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def get_body(self):
        body = Body()
        body.shape = "coupe"
        return body

    def get_engine(self):
        engine = Engine()
        engine.power = 250
        return engine


class Director:
    _builder = None

    def set_builder(self, builder):
        self._builder = builder

    def construct(self):
        car = Car()
        body = self._builder.get_body()
        car.set_body(body=body)

        engine = self._builder.get_engine()
        car.set_engine(engine)

        wheel = self._builder.get_wheel()
        car.set_wheel(wheel)

        return car


def client_builder(builder):
    builders = {"benz": Benz, "bmw": Bmw}

    car = builders[builder]()
    director = Director()
    director.set_builder(car)
    result = director.construct()
    return result.detail()


client_builder('benz')
