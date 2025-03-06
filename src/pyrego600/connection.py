from abc import ABC


class Connection(ABC):
    @property
    def is_connected(self) -> bool:
        raise NotImplementedError

    async def connect(self) -> None:
        raise NotImplementedError

    async def close(self) -> None:
        raise NotImplementedError

    async def read(self, length: int) -> bytes:
        raise NotImplementedError

    async def write(self, buffer: bytes) -> None:
        raise NotImplementedError
