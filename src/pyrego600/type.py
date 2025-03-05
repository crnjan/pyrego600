from enum import Enum, auto


class Type(Enum):
    TEMPERATURE = auto()
    SWITCH = auto()
    HOURS = auto()
    UNITLESS = auto()
