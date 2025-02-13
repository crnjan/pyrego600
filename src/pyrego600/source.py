from dataclasses import dataclass


@dataclass(frozen=True)
class Source:
    read: int
    write: int | None = None
