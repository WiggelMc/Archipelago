from abc import ABC
from dataclasses import dataclass

from . import common_values
from .item_provider_base import ItemProvider, PoolItem, ItemType
from .option_provider_base import EnumOptionProvider
from .requirements_base import Requirement
from .string_case_utils import to_case, NameCase


class StackedItemDefinition(EnumOptionProvider, ItemProvider, ABC):
    pass


class AutoPoolItem(PoolItem):
    id_offset: int


@dataclass(kw_only=True)
class SingleItem(AutoPoolItem):
    id_offset: int
    name: str = None
    type: ItemType = ItemType.PROGRESSION
    id: int = None


@dataclass(kw_only=True)
class SingleReqItem(SingleItem, Requirement):
    pass


@dataclass(kw_only=True)
class ProgressiveItem(AutoPoolItem):
    id_offset: int
    name: str = None
    type: ItemType = ItemType.PROGRESSION
    id: int = None


@dataclass(kw_only=True)
class ProgressiveReqItem(ProgressiveItem, Requirement):
    pass


@dataclass(kw_only=True)
class SeperateItem(AutoPoolItem):
    id_offset: int
    name: str
    stage: int
    type: ItemType = ItemType.PROGRESSION
    id: int = None


@dataclass(kw_only=True)
class SeperateReqItem(SeperateItem, Requirement):
    pass


def generate_items(items: list[AutoPoolItem], name_pascal: str):
    name_word = to_case(name_pascal, NameCase.Pascal, NameCase.WordTitle)
    for item in items:
        if (item.id is None) and (item.id_offset is not None):
            item.id = item.id_offset + common_values.item_base_id
        if not item.name:
            match item:
                case ProgressiveItem():
                    item.name = f"{common_values.progressive_item_prefix_word} {name_word}"
                case _:
                    item.name = name_word
