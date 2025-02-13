from dataclasses import dataclass

from .transformation import Transformation


@dataclass(frozen=True)
class NumericTransformation(Transformation):
    multiplier: float

    def toValue(self, value: float) -> float:
        # This value marks "absence" of a sensor
        if value == -483:
            return None
        return round(value * self.multiplier * 1 / self.multiplier) / (1 / self.multiplier)

    def fromValue(self, value: float) -> float:
        return value / self.multiplier
