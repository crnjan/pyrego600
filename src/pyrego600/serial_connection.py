import serial_asyncio_fast as serial_asyncio

from .connection import Connection


class SerialConnection(Connection):
    def __init__(self, url) -> None:
        self.__url = url
        self.__reader = None
        self.__writter = None

    @property
    def is_connected(self) -> bool:
        return self.__reader is not None

    async def connect(self) -> None:
        self.__reader, self.__writter = await serial_asyncio.open_serial_connection(url=self.__url, baudrate=19200)

    async def close(self) -> None:
        if self.__writter is not None:
            self.__writter.close()
            await self.__writter.wait_closed()
        self.__writter = None
        self.__reader = None

    async def read(self, length: int) -> bytes:
        return await self.__reader.readexactly(length)

    async def write(self, buffer: bytes) -> None:
        self.__writter.write(buffer)
        await self.__writter.drain()
