from abc import abstractmethod

from item_info import ParaboxItemInfoDefinitions as Items, ParaboxItemType, ParaboxItemInfo
from opt.logic_option_values import FixBanishmentValues
from opt.option_base_values import ShuffleOptionValues, ShuffleProgressiveOptionValues, \
    ShuffleProgressiveOrSeperateOptionValues
from opt.shuffle_option_values import ShuffleLevelSelectValues
from opt.world_option_values import WorldGenerationValues, LevelGenerationValues
from option_values import ParaboxOptionValues


class ParaboxItemDataCreator:
    @classmethod
    @abstractmethod
    def create_items(cls, options: ParaboxOptionValues) -> list[ParaboxItemInfo]:
        pass


# noinspection PyUnusedLocal
class ParaboxShuffleItemDataCreator(ParaboxItemDataCreator):
    items_single: list[ParaboxItemInfo] = []

    @staticmethod
    @abstractmethod
    def get_option(options: ParaboxOptionValues) -> int:
        pass

    @classmethod
    def get_items_single(cls, options: ParaboxOptionValues):
        return cls.items_single

    @classmethod
    def create_items(cls, options: ParaboxOptionValues) -> list[ParaboxItemInfo]:
        option = cls.get_option(options)
        match option:
            case ShuffleOptionValues.option_single:
                return cls.get_items_single(options)
            case _:
                return []


# noinspection PyUnusedLocal
class ParaboxProgressiveShuffleItemDataCreator(ParaboxItemDataCreator):
    items_single: list[ParaboxItemInfo] = []
    items_progressive: list[ParaboxItemInfo] = []

    @staticmethod
    @abstractmethod
    def get_option(options: ParaboxOptionValues) -> int:
        pass

    @classmethod
    def get_items_single(cls, options: ParaboxOptionValues):
        return cls.items_single

    @classmethod
    def get_items_progressive(cls, options: ParaboxOptionValues):
        return cls.items_progressive

    @classmethod
    def create_items(cls, options: ParaboxOptionValues) -> list[ParaboxItemInfo]:
        option = cls.get_option(options)
        match option:
            case ShuffleProgressiveOptionValues.option_single:
                return cls.get_items_single(options)
            case ShuffleProgressiveOptionValues.option_progressive:
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
    def get_option(options: ParaboxOptionValues) -> int:
        pass

    @classmethod
    def get_items_single(cls, options: ParaboxOptionValues):
        return cls.items_single

    @classmethod
    def get_items_progressive(cls, options: ParaboxOptionValues):
        return cls.items_progressive

    @classmethod
    def get_items_seperate(cls, options: ParaboxOptionValues):
        return cls.items_seperate

    @classmethod
    def create_items(cls, options: ParaboxOptionValues) -> list[ParaboxItemInfo]:
        option = cls.get_option(options)
        match option:
            case ShuffleProgressiveOrSeperateOptionValues.option_single:
                return cls.get_items_single(options)
            case ShuffleProgressiveOrSeperateOptionValues.option_progressive:
                return cls.get_items_progressive(options)
            case ShuffleProgressiveOrSeperateOptionValues.option_seperate:
                return cls.get_items_seperate(options)
            case _:
                return []


class PriorityItemDataCreator(ParaboxShuffleItemDataCreator):
    @staticmethod
    def get_option(options: ParaboxOptionValues) -> int:
        return options.shuffle_priority

    items_single = [Items.priority]


class UndoItemDataCreator(ParaboxProgressiveShuffleItemDataCreator):
    @staticmethod
    def get_option(options: ParaboxOptionValues) -> int:
        return options.shuffle_undo

    @staticmethod
    def get_undo_type(options: ParaboxOptionValues):
        if (
                options.shuffle_level_select != ShuffleLevelSelectValues.option_disabled
                and options.fix_banishment == FixBanishmentValues.option_vanilla
                and options.world_generation not in [
                    WorldGenerationValues.option_vanilla, WorldGenerationValues.option_shuffle]
                and options.level_generation == LevelGenerationValues.option_randomize
        ):
            return ParaboxItemType.PROGRESSION
        else:
            return ParaboxItemType.USEFUL

    @classmethod
    def get_items_single(cls, options: ParaboxOptionValues):
        undo_type = cls.get_undo_type(options)
        return [Items.undo.typed(undo_type)] * (1 + options.undo_extra_copy_count)

    @classmethod
    def get_items_progressive(cls, options: ParaboxOptionValues):
        undo_type = cls.get_undo_type(options)
        return [Items.progressive_undo.typed(undo_type)] * (2 + options.undo_extra_copy_count)


class PossessItemDataCreator(ParaboxProgressiveOrSeperateShuffleItemDataCreator):
    @staticmethod
    def get_option(options: ParaboxOptionValues) -> int:
        return options.shuffle_possess

    items_single = [Items.possess]
    items_progressive = [Items.progressive_possess] * 2
    items_seperate = [Items.possess_box, Items.possess_wall]


if __name__ == '__main__':
    print("")
    # TODO seperate AP code from Options to be able to use them on the client
