from __future__ import annotations

from abc import abstractmethod
from enum import Enum

from .generator import Generator


class ItemType(Enum):
    PROGRESSION = 1
    USEFUL = 2
    TRAP = 3


class Item:
    name: str
    id: int


class PoolItem(Item):
    type: ItemType


item_providers: list[ItemProvider] = []


class ItemProvider(Generator):
    @classmethod
    def _generate(cls):
        item_providers.append(cls())
        super()._generate()

    @classmethod
    @abstractmethod
    def pool_items(cls, options: dict[str, int]) -> list[PoolItem]:
        pass

    items: list[Item]
