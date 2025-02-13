from .decoders import Decoders
from .identifier import Identifier
from .register import Register
from .sources import Sources
from .transformations import Transformations
from .type import Type


class RegisterFactory:
    @staticmethod
    def version(identifier: Identifier) -> Register:
        return Register(
            identifier=identifier,
            source=Sources.VERSION,
            address=0x0000,
            decoder=Decoders.INT_16,
            transformation=Transformations.IDENTITY,
            type=None,
        )

    @staticmethod
    def lastError(identifier: Identifier) -> Register:
        return Register(
            identifier=identifier,
            source=Sources.LAST_ERROR,
            address=0x0000,
            decoder=Decoders.ERROR,
            transformation=Transformations.IDENTITY,
            type=None,
        )

    @staticmethod
    def frontPanelSwitch(identifier: Identifier, address: int) -> Register:
        return Register(
            identifier=identifier,
            source=Sources.FRONT_PANEL,
            address=address,
            decoder=Decoders.INT_16,
            transformation=Transformations.IDENTITY,
            type=Type.SWITCH,
        )

    @staticmethod
    def systemTemperature(identifier: Identifier, address: int) -> Register:
        return Register(
            identifier=identifier,
            source=Sources.SYSTEM,
            address=address,
            decoder=Decoders.INT_16,
            transformation=Transformations.NUMERIC_ONE_TENTH,
            type=Type.TEMPERATURE,
        )

    @staticmethod
    def systemSwitch(identifier: Identifier, address: int) -> Register:
        return Register(
            identifier=identifier,
            source=Sources.SYSTEM,
            address=address,
            decoder=Decoders.INT_16,
            transformation=Transformations.IDENTITY,
            type=Type.SWITCH,
        )

    @staticmethod
    def systemHours(identifier: Identifier, address: int) -> Register:
        return Register(
            identifier=identifier,
            source=Sources.SYSTEM,
            address=address,
            decoder=Decoders.INT_16,
            transformation=Transformations.IDENTITY,
            type=Type.HOURS,
        )
