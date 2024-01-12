from typing import NamedTuple

from BaseClasses import Item
from worlds.parabox import PARABOX_GAME


class ParaboxItem(Item):
    game: str = PARABOX_GAME


class ParaboxItemData(NamedTuple):
    id: int
    type: str


class ParaboxItemDataCreator:
    def __init__(self):
        pass

    def get_single(self) -> dict[str, ParaboxItem]:
        return {}


class ParaboxProgressiveItemDataCreator(ParaboxItemDataCreator):
    def __init__(self):
        super().__init__()

    def get_progressive(self) -> dict[str, ParaboxItem]:
        return {}


class ParaboxProgressiveOrSeperateItemDataCreator(ParaboxProgressiveItemDataCreator):
    def __init__(self):
        super().__init__()

    def get_seperate(self) -> dict[str, ParaboxItem]:
        return {}
