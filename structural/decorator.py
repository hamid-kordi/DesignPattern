"""
Decorator

- a structural pattern that allows adding new behaviors to objects dynamically
by placing them inside special wrapper objects, called decorators.

"""

from abc import ABC, abstractmethod


class Page(ABC):  # adstract component
    @abstractmethod
    def show(self):
        pass


class AuthPage(Page):  # concrete component  1
    def show(self):
        print("welcome to authenticated page...")


class AnonPage(Page):  # concrete component  2
    def show(self):
        print("welcome to anonymous page...")


class PageDecorate(Page, ABC):  # abstract decorator
    def __init__(self, component):
        self._component = component

    @abstractmethod
    def show(self):
        pass


class PageAuthDecorator(PageDecorate):
    def show(self):
        username = input("enter your username")
        password = input("enter your password")
        if username == "admin" and password == "1234":
            self._component.show()
        else:
            print("your not authenticated")


def client_decorator():
    page = AuthPage()
    auth = PageAuthDecorator(page)
    auth.show()


client_decorator()
