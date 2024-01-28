from abc import abstractmethod
from enum import Enum


class ItemType(Enum):
    PROGRESSION = 1
    USEFUL = 2
    TRAP = 3


class Item:
    name: str
    id: int


class PoolItem(Item):
    type: ItemType


class ItemProvider:
    @classmethod
    @abstractmethod
    def pool_items(cls, options: dict[str, int]) -> list[PoolItem]:
        pass

    items: list[Item]
