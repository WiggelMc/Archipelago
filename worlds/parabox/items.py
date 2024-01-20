from abc import abstractmethod
from enum import Enum
from typing import NamedTuple

from BaseClasses import Item
from worlds.parabox import PARABOX_GAME, ParaboxOptions
from worlds.parabox.opt.option_base import ShuffleOption, ShuffleProgressiveOption, ShuffleProgressiveOrSeperateOption


class ParaboxItem(Item):
    game: str = PARABOX_GAME


class ParaboxItemType(Enum):
    PROGRESSION = 1
    USEFUL = 2
    TRAP = 3


class ParaboxItemData(NamedTuple):
    id: int
    type: ParaboxItemType


class ParaboxItemDefinition(NamedTuple):
    name: str
    item: ParaboxItemData


class ParaboxItemDataCreator:
    @classmethod
    @abstractmethod
    def create_items(cls, options: ParaboxOptions) -> list[ParaboxItemDefinition]:
        pass


class ParaboxShuffleItemDataCreator(ParaboxItemDataCreator):
    items_single: list[ParaboxItemDefinition] = []

    @staticmethod
    @abstractmethod
    def get_option(options: ParaboxOptions) -> ShuffleOption:
        pass

    @classmethod
    def create_items(cls, options: ParaboxOptions) -> list[ParaboxItemDefinition]:
        option = cls.get_option(options)
        match option:
            case ShuffleOption.option_single:
                return cls.items_single
            case _:
                return []


class ParaboxProgressiveShuffleItemDataCreator(ParaboxItemDataCreator):
    items_single: list[ParaboxItemDefinition] = []
    items_progressive: list[ParaboxItemDefinition] = []

    @staticmethod
    @abstractmethod
    def get_option(options: ParaboxOptions) -> ShuffleProgressiveOption:
        pass

    @classmethod
    def create_items(cls, options: ParaboxOptions) -> list[ParaboxItemDefinition]:
        option = cls.get_option(options)
        match option:
            case ShuffleProgressiveOption.option_single:
                return cls.items_single
            case ShuffleProgressiveOption.option_progressive:
                return cls.items_progressive
            case _:
                return []


class ParaboxProgressiveOrSeperateShuffleItemDataCreator(ParaboxItemDataCreator):
    items_single: list[ParaboxItemDefinition] = []
    items_progressive: list[ParaboxItemDefinition] = []
    items_seperate: list[ParaboxItemDefinition] = []

    @staticmethod
    @abstractmethod
    def get_option(options: ParaboxOptions) -> ShuffleProgressiveOrSeperateOption:
        pass

    @classmethod
    def create_items(cls, options: ParaboxOptions) -> list[ParaboxItemDefinition]:
        option = cls.get_option(options)
        match option:
            case ShuffleProgressiveOrSeperateOption.option_single:
                return cls.items_single
            case ShuffleProgressiveOrSeperateOption.option_progressive:
                return cls.items_progressive
            case ShuffleProgressiveOrSeperateOption.option_seperate:
                return cls.items_seperate
            case _:
                return []


class ParaboxItemTable:
    priority \
        = ParaboxItemDefinition("Priority",
                                ParaboxItemData(1, ParaboxItemType.PROGRESSION))
    extrude \
        = ParaboxItemDefinition("Extrude",
                                ParaboxItemData(2, ParaboxItemType.PROGRESSION))
    inner_push \
        = ParaboxItemDefinition("Inner Push",
                                ParaboxItemData(3, ParaboxItemType.PROGRESSION))
    block \
        = ParaboxItemDefinition("Block",
                                ParaboxItemData(4, ParaboxItemType.PROGRESSION))
    level_select \
        = ParaboxItemDefinition("Level Select",
                                ParaboxItemData(5, ParaboxItemType.PROGRESSION))
    clone \
        = ParaboxItemDefinition("Clone",
                                ParaboxItemData(6, ParaboxItemType.PROGRESSION))
    open_main_level \
        = ParaboxItemDefinition("Open Main Level",
                                ParaboxItemData(7, ParaboxItemType.PROGRESSION))
    even \
        = ParaboxItemDefinition("Even",
                                ParaboxItemData(8, ParaboxItemType.PROGRESSION))
    oblong \
        = ParaboxItemDefinition("Oblong",
                                ParaboxItemData(9, ParaboxItemType.PROGRESSION))
    one \
        = ParaboxItemDefinition("One",
                                ParaboxItemData(10, ParaboxItemType.PROGRESSION))

    recursion \
        = ParaboxItemDefinition("Recursion",
                                ParaboxItemData(11, ParaboxItemType.PROGRESSION))
    progressive_recursion \
        = ParaboxItemDefinition("Progressive Recursion",
                                ParaboxItemData(12, ParaboxItemType.PROGRESSION))
    flip \
        = ParaboxItemDefinition("Flip",
                                ParaboxItemData(13, ParaboxItemType.PROGRESSION))
    progressive_flip \
        = ParaboxItemDefinition("Progressive Flip",
                                ParaboxItemData(14, ParaboxItemType.PROGRESSION))
    friend \
        = ParaboxItemDefinition("Friend",
                                ParaboxItemData(15, ParaboxItemType.PROGRESSION))
    progressive_friend \
        = ParaboxItemDefinition("Progressive Friend",
                                ParaboxItemData(16, ParaboxItemType.PROGRESSION))
    infinite_exit_block \
        = ParaboxItemDefinition("Infinite Exit",
                                ParaboxItemData(17, ParaboxItemType.PROGRESSION))
    progressive_infinite_exit_block \
        = ParaboxItemDefinition("Progressive Infinite Exit",
                                ParaboxItemData(18, ParaboxItemType.PROGRESSION))
    infinite_enter_block \
        = ParaboxItemDefinition("Infinite Enter",
                                ParaboxItemData(19, ParaboxItemType.PROGRESSION))
    progressive_infinite_enter_block \
        = ParaboxItemDefinition("Progressive Infinite Enter",
                                ParaboxItemData(20, ParaboxItemType.PROGRESSION))
    player \
        = ParaboxItemDefinition("Player",
                                ParaboxItemData(21, ParaboxItemType.PROGRESSION))
    progressive_player \
        = ParaboxItemDefinition("Progressive Player",
                                ParaboxItemData(22, ParaboxItemType.PROGRESSION))
    undo \
        = ParaboxItemDefinition("Undo",
                                ParaboxItemData(23, ParaboxItemType.PROGRESSION))
    progressive_undo \
        = ParaboxItemDefinition("Progressive Undo",
                                ParaboxItemData(24, ParaboxItemType.PROGRESSION))

    possess \
        = ParaboxItemDefinition("Possess",
                                ParaboxItemData(25, ParaboxItemType.PROGRESSION))
    progressive_possess \
        = ParaboxItemDefinition("Progressive Possess",
                                ParaboxItemData(26, ParaboxItemType.PROGRESSION))
    possess_wall \
        = ParaboxItemDefinition("Possess Wall",
                                ParaboxItemData(27, ParaboxItemType.PROGRESSION))
    possess_box \
        = ParaboxItemDefinition("Possess Box",
                                ParaboxItemData(28, ParaboxItemType.PROGRESSION))


class PriorityItemDataCreator(ParaboxShuffleItemDataCreator):
    def get_option(self, options: ParaboxOptions) -> ShuffleOption:
        return options.shuffle_priority

    items_single = [ParaboxItemTable.priority]


class UndoItemDataCreator(ParaboxProgressiveShuffleItemDataCreator):
    def get_option(self, options: ParaboxOptions) -> ShuffleProgressiveOption:
        return options.shuffle_undo

    items_single = [ParaboxItemTable.undo]
    items_progressive = [ParaboxItemTable.progressive_undo] * 2


class PossessItemDataCreator(ParaboxProgressiveOrSeperateShuffleItemDataCreator):
    def get_option(self, options: ParaboxOptions) -> ShuffleProgressiveOrSeperateOption:
        return options.shuffle_possess

    items_single = [ParaboxItemTable.possess]
    items_progressive = [ParaboxItemTable.progressive_possess] * 2
    items_seperate = [ParaboxItemTable.possess_box, ParaboxItemTable.possess_wall]
