from ..value_converter import sevenBitFormatToInt16
from .abstract_decoder import AbstractDecoder


class Int16Decoder(AbstractDecoder):
    @property
    def length(self) -> int:
        return 5

    def _convert(self, buffer: bytes) -> int:
        return sevenBitFormatToInt16(buffer, 1)
