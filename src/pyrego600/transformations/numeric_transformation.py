from dataclasses import dataclass

from .transformation import Transformation


@dataclass(frozen=True)
class NumericTransformation(Transformation):
    multiplier: float

    def to_value(self, value: int) -> float:
        # This value marks "absence" of a sensor
        if value == -483:
            return None
        return round(value * self.multiplier * 1 / self.multiplier) / (1 / self.multiplier)

    def from_value(self, value: float) -> int:
        return round(value / self.multiplier)
