# approach no.1
from typing import Any


class A:
    _instance = None

    def __init__(self) -> None:
        raise RuntimeError("call get_instance() instead")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance


one = A.get_instance()
two = A.get_instance()


print(id(one))
print(id(two))


# approach no.2


class Singleton(type):
    _instance = None

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class B(metaclass=Singleton):
    pass


one = B()
two = B()

print(one, two)
