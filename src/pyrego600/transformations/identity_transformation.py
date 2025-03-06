from ..last_error import LastError
from .transformation import Transformation


class IdentityTransformation(Transformation):
    def to_value(self, value: int | LastError | None) -> int | LastError | None:
        return value

    def from_value(self, value: float) -> int:
        return value
