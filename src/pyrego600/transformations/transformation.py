from abc import ABC


class Transformation(ABC):
    def toValue(self, value: float) -> float:
        raise NotImplementedError

    def fromValue(self, value: float) -> float:
        raise NotImplementedError
