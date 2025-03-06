from .abstract_decoder import AbstractDecoder


class EmptyDecoder(AbstractDecoder):
    @property
    def length(self) -> int:
        return 1

    def _convert(self, buffer: bytes) -> int:
        return 0
