"""

Observer
- behavioral design pattern that lets you define a subscription mechanism to notify 
    multiple objects about any events that happen to the object they're observing

"""

import abc
from random import randrange


class Publisher(abc.ABC):
    @abc.abstractmethod
    def subscribe():
        pass

    @abc.abstractmethod
    def unsubscribe():
        pass

    @abc.abstractmethod
    def notify():
        pass


class ConcretePublisher(Publisher):

    _observer = []
    _state = None

    def subscribe(self,observer):
        self._observer.append(observer)

    def unsubscribe(self,observer):
        self._observer.remove(observer)

    def notify(self):
        print("notify all . . . ")

        for observer in self._observer:
            observer.update()

    def operation(self):
        self._state = randrange(0,10)
        print(f'self._state = {self._state}')
        self.notify()


class Observer(abc.ABC):
    @abc.abstractmethod
    def update(self,publisher):
        pass


class ObserverA(Observer):
    def update(self, publisher):
        if publisher._state <= 5:
            print('ObserverA reacted to the event')


class ObserverB(Observer):
    def update(self, publisher):
        if publisher._state > 5:
            print('ObserverB reacted to the event')


publisher = ConcretePublisher()
oba = ObserverA()
obb = ObserverB()

publisher.subscribe(oba)
publisher.subscribe(obb)


publisher.operation()