from abc import ABC

from ..last_error import LastError


class Transformation(ABC):
    def to_value(self, value: int | LastError | None) -> int | LastError | None:
        raise NotImplementedError

    def from_value(self, value: float) -> int:
        raise NotImplementedError
