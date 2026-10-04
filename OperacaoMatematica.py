from abc import abstractmethod, ABC


class Opmm(ABC):

    @abstractmethod
    def op(self, n1, n2):
        pass