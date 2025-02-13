from ..value_converter import arrayToByte, stringFromBytes
from .abstract_decoder import AbstractDecoder


class ErrorDecoder(AbstractDecoder):
    @property
    def length(self) -> int:
        return 42

    def _convert(self, buffer: bytes) -> str | None:
        if buffer[1] == 0xFF:
            return None
        return (arrayToByte(buffer, 1), stringFromBytes(buffer, 3, 15))
