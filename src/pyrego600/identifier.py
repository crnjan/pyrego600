from dataclasses import dataclass

from .group import Group


@dataclass(frozen=True)
class Identifier:
    id: str
    group: Group

    def __str__(self):
        return f"{self.group.value}-{self.id}"
