from abc import ABC
from dataclasses import dataclass

from .item_provider_base import ItemProvider, PoolItem, ItemType
from .option_provider_base import EnumOptionProvider
from .requirements_base import Requirement


class StackedItemDefinition(EnumOptionProvider, ItemProvider, ABC):
    pass


class RelativePoolItem(PoolItem):
    id_offset: int


@dataclass(kw_only=True)
class SingleItem(RelativePoolItem):
    id_offset: int
    name: str = None
    type: ItemType = ItemType.PROGRESSION
    id: int = None


@dataclass(kw_only=True)
class SingleReqItem(SingleItem, Requirement):
    pass


@dataclass(kw_only=True)
class ProgressiveItem(RelativePoolItem):
    id_offset: int
    name: str = None
    type: ItemType = ItemType.PROGRESSION
    id: int = None


@dataclass(kw_only=True)
class ProgressiveReqItem(ProgressiveItem, Requirement):
    pass


@dataclass(kw_only=True)
class SeperateItem(RelativePoolItem):
    id_offset: int
    progressive_level: int
    name: str = None
    type: ItemType = ItemType.PROGRESSION
    id: int = None


@dataclass(kw_only=True)
class SeperateReqItem(SeperateItem, Requirement):
    pass
