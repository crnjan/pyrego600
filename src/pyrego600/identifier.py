from dataclasses import dataclass

from .group import Group


@dataclass(frozen=True)
class Identifier:
    id: str
    group: Group
