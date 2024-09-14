import abc


class Read:
    def __init__(self, sentence) -> None:
        self.sentence = sentence
        self._direction = None

    def set_directions(self, direction):
        self._direction = direction

    def read(self):
        self._direction.direct(self.sentence)


class Directions(abc.ABC):
    @abc.abstractmethod
    def direct(self, data):
        pass


class L2r(Directions):
    def direct(self, data):
        print(data[::-1])


class R2l(Directions):
    def direct(self, data):
        print(data[::1])


r = Read("hello world")
l2r = L2r()
r2l = R2l()
r.set_directions(l2r)
r.read()
r.set_directions(r2l)
r.read()
