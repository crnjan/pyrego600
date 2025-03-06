from abc import ABC

from ..last_error import LastError


class Decoder(ABC):
    @property
    def length(self) -> int:
        raise NotImplementedError

    def decode(self, buffer: bytes) -> int | LastError | None:
        raise NotImplementedError
