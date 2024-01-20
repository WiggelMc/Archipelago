import typing
from abc import abstractmethod

from worlds.parabox.item_info import ParaboxItemInfoDefinitions as Items, ParaboxItemType, ParaboxItemInfo

if typing.TYPE_CHECKING:
    from worlds.parabox.opt.option_base import ShuffleOption, ShuffleProgressiveOption, \
        ShuffleProgressiveOrSeperateOption
    from worlds.parabox.options import ParaboxOptions


class ParaboxItemDataCreator:
    @classmethod
    @abstractmethod
    def create_items(cls, options: ParaboxOptions) -> list[ParaboxItemInfo]:
        pass


# noinspection PyUnusedLocal
class ParaboxShuffleItemDataCreator(ParaboxItemDataCreator):
    items_single: list[ParaboxItemInfo] = []

    @staticmethod
    @abstractmethod
    def get_option(options: ParaboxOptions) -> ShuffleOption:
        pass

    @classmethod
    def get_items_single(cls, options: ParaboxOptions):
        return cls.items_single

    @classmethod
    def create_items(cls, options: ParaboxOptions) -> list[ParaboxItemInfo]:
        option = cls.get_option(options)
        match option:
            case ShuffleOption.option_single:
                return cls.get_items_single(options)
            case _:
                return []


# noinspection PyUnusedLocal
class ParaboxProgressiveShuffleItemDataCreator(ParaboxItemDataCreator):
    items_single: list[ParaboxItemInfo] = []
    items_progressive: list[ParaboxItemInfo] = []

    @staticmethod
    @abstractmethod
    def get_option(options: ParaboxOptions) -> ShuffleProgressiveOption:
        pass

    @classmethod
    def get_items_single(cls, options: ParaboxOptions):
        return cls.items_single

    @classmethod
    def get_items_progressive(cls, options: ParaboxOptions):
        return cls.items_progressive

    @classmethod
    def create_items(cls, options: ParaboxOptions) -> list[ParaboxItemInfo]:
        option = cls.get_option(options)
        match option:
            case ShuffleProgressiveOption.option_single:
                return cls.get_items_single(options)
            case ShuffleProgressiveOption.option_progressive:
                return cls.get_items_progressive(options)
            case _:
                return []


# noinspection PyUnusedLocal
class ParaboxProgressiveOrSeperateShuffleItemDataCreator(ParaboxItemDataCreator):
    items_single: list[ParaboxItemInfo] = []
    items_progressive: list[ParaboxItemInfo] = []
    items_seperate: list[ParaboxItemInfo] = []

    @staticmethod
    @abstractmethod
    def get_option(options: ParaboxOptions) -> ShuffleProgressiveOrSeperateOption:
        pass

    @classmethod
    def get_items_single(cls, options: ParaboxOptions):
        return cls.items_single

    @classmethod
    def get_items_progressive(cls, options: ParaboxOptions):
        return cls.items_progressive

    @classmethod
    def get_items_seperate(cls, options: ParaboxOptions):
        return cls.items_seperate

    @classmethod
    def create_items(cls, options: ParaboxOptions) -> list[ParaboxItemInfo]:
        option = cls.get_option(options)
        match option:
            case ShuffleProgressiveOrSeperateOption.option_single:
                return cls.get_items_single(options)
            case ShuffleProgressiveOrSeperateOption.option_progressive:
                return cls.get_items_progressive(options)
            case ShuffleProgressiveOrSeperateOption.option_seperate:
                return cls.get_items_seperate(options)
            case _:
                return []


class PriorityItemDataCreator(ParaboxShuffleItemDataCreator):
    @staticmethod
    def get_option(options: ParaboxOptions) -> ShuffleOption:
        return options.shuffle_priority

    items_single = [Items.priority]


class UndoItemDataCreator(ParaboxProgressiveShuffleItemDataCreator):
    @staticmethod
    def get_option(options: ParaboxOptions) -> ShuffleProgressiveOption:
        return options.shuffle_undo

    @staticmethod
    def get_undo_type(options: ParaboxOptions):
        if (
                options.shuffle_level_select != ParaboxOptions.shuffle_level_select.option_disabled
                and options.fix_banishment == ParaboxOptions.fix_banishment.option_vanilla
                and options.world_generation != ParaboxOptions.world_generation.option_normal
                and options.level_generation == ParaboxOptions.level_generation.option_randomize
        ):
            return ParaboxItemType.PROGRESSION
        else:
            return ParaboxItemType.USEFUL

    @classmethod
    def get_items_single(cls, options: ParaboxOptions):
        undo_type = cls.get_undo_type(options)
        return [Items.undo.typed(undo_type)] * (1 + options.undo_extra_copy_count)

    @classmethod
    def get_items_progressive(cls, options: ParaboxOptions):
        undo_type = cls.get_undo_type(options)
        return [Items.progressive_undo.typed(undo_type)] * (2 + options.undo_extra_copy_count)


class PossessItemDataCreator(ParaboxProgressiveOrSeperateShuffleItemDataCreator):
    @staticmethod
    def get_option(options: ParaboxOptions) -> ShuffleProgressiveOrSeperateOption:
        return options.shuffle_possess

    items_single = [Items.possess]
    items_progressive = [Items.progressive_possess] * 2
    items_seperate = [Items.possess_box, Items.possess_wall]


if __name__ == '__main__':
    print("")
    # TODO seperate AP code from Options to be able to use them on the client
