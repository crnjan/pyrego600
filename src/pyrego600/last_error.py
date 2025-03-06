import datetime
from typing import NamedTuple


class LastError(NamedTuple):
    code: int
    timestamp: datetime
