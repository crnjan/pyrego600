from abc import ABC


class Decoder(ABC):
    @property
    def length(self) -> int:
        raise NotImplementedError

    def decode(self, buffer: bytes) -> int | float | str:
        raise NotImplementedError
