from .transformation import Transformation


class IdentityTransformation(Transformation):
    def toValue(self, value: float) -> float:
        return value

    def fromValue(self, value: float) -> float:
        return value
