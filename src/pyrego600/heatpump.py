"""Provides TODO."""

import asyncio
import logging
from asyncio import timeout as asyncio_timeout

from .connection import Connection
from .decoders import Decoder
from .register import Register
from .register_repository import RegisterRepository
from .regoerror import RegoError
from .transformations import Transformation

_LOGGER = logging.getLogger(__name__)
_RETRIES: int = 3


class HeatPump:
    def __init__(self, connection: Connection) -> None:
        self.__connection = connection

    @property
    def registers(self) -> list[Register]:
        """Return the register database."""
        return RegisterRepository.registers()

    async def dispose(self):
        await self.__connection.close()

    async def verify(self, retry: int = _RETRIES) -> None:
        _LOGGER.debug("Reading Rego device version...")
        register = RegisterRepository.version()
        version = await self.__send(*register._read(), retry)
        if version != 600:
            await self.__connection.close()
            raise RegoError(f"Invalid rego version received {version}")
        _LOGGER.debug(f"Connected to Rego version {version}.")

    async def read(self, register: Register, retry: int = _RETRIES) -> float:
        return await self.__send(*register._read(), retry)

    async def write(self, register: Register, value: float, retry: int = _RETRIES) -> None:
        transformed = register.transformation.fromValue(value)
        return await self.__send(*register._write(round(transformed)), retry)

    async def __send(self, payload: bytes, decoder: Decoder, transformation: Transformation, retry: int) -> float:
        try:
            if not self.__connection.isConnected:
                _LOGGER.debug("Not connected, connecting...")
                await self.__connection.connect()
                _LOGGER.debug("Connected")

            # Give heat pump some time between commands. Feeding commands too quickly
            # might cause heat pump not to respond.
            await asyncio.sleep(0.05)

            async with asyncio_timeout(2):
                _LOGGER.debug(f"Sending '{payload.hex()}'")
                await self.__connection.write(payload)
                _LOGGER.debug("Send, waiting for response...")
                response = await self.__connection.read(decoder.length)
                _LOGGER.debug(f"Received {response.hex()}")
            return transformation.toValue(decoder.decode(response))

        except (OSError, RegoError) as e:
            _LOGGER.debug(f"Sending '{payload.hex()}' failed due {e!r}")
            await self.__connection.close()
            if retry > 0:
                _LOGGER.debug(f"Retrying, {retry=}")
                await asyncio.sleep(0.2)
                return await self.__send(payload, decoder, transformation, retry - 1)
            raise
