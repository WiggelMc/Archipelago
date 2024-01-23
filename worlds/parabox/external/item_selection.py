from abc import abstractmethod

from item_info import ParaboxItemInfoDefinitions as Items, ParaboxItemType, ParaboxItemInfo, ParaboxSingleItemInfo, \
    ParaboxProgressiveItemInfo, ParaboxSeperateItemInfo
from opt.logic_option_values import FixBanishmentValues
from opt.option_base_values import ShuffleProgressiveOrSeperateOptionValues
from opt.shuffle_option_values import ShuffleLevelSelectValues
from opt.world_option_values import WorldGenerationValues, LevelGenerationValues
from option_values import ParaboxOptionValues, option_values_from_dict


class ParaboxItemDataCreator:
    @classmethod
    @abstractmethod
    def create_items(cls, options: ParaboxOptionValues) -> list[ParaboxItemInfo]:
        pass


# noinspection PyUnusedLocal
class ParaboxShuffleItemDataCreator(ParaboxItemDataCreator):
    items: list[ParaboxItemInfo] = []

    @staticmethod
    @abstractmethod
    def get_option(options: ParaboxOptionValues) -> int:
        pass

    @classmethod
    def get_items(cls, options: ParaboxOptionValues):
        return cls.items

    @classmethod
    def modify_items(cls, item_list: list[ParaboxItemInfo], options: ParaboxOptionValues) -> list[ParaboxItemInfo]:
        return item_list

    @classmethod
    def get_items_single(cls, options: ParaboxOptionValues):
        item_list: list[ParaboxItemInfo] = cls.get_items(options)
        if not item_list:
            return []
        match item_list[0]:
            case ParaboxSingleItemInfo():
                item_list: list[ParaboxSingleItemInfo]
                return list(set(item_list))
            case ParaboxProgressiveItemInfo():
                item_list: list[ParaboxProgressiveItemInfo]
                return list(set([item.single_item for item in item_list]))
            case ParaboxSeperateItemInfo():
                item_list: list[ParaboxSeperateItemInfo]
                return list(set([item.progressive_item.single_item for item in item_list]))
            case _:
                raise Exception(f"Invalid Item Type {type(item_list[0])} for list {item_list}")

    @classmethod
    def get_items_progressive(cls, options: ParaboxOptionValues):
        item_list: list[ParaboxItemInfo] = cls.get_items(options)
        if not item_list:
            return []
        match item_list[0]:
            case ParaboxProgressiveItemInfo():
                item_list: list[ParaboxProgressiveItemInfo]
                return item_list
            case ParaboxSeperateItemInfo():
                item_list: list[ParaboxSeperateItemInfo]
                item_count = max([item.n for item in item_list])
                return [item_list[0].progressive_item] * item_count
            case _:
                raise Exception(f"Invalid Item Type {type(item_list[0])} for list {item_list}")

    @classmethod
    def get_items_seperate(cls, options: ParaboxOptionValues):
        item_list: list[ParaboxItemInfo] = cls.get_items(options)
        if not item_list:
            return []
        match item_list[0]:
            case ParaboxSeperateItemInfo():
                item_list: list[ParaboxSeperateItemInfo]
                return item_list
            case _:
                raise Exception(f"Invalid Item Type {type(item_list[0])} for list {item_list}")

    @classmethod
    def create_items(cls, options: ParaboxOptionValues) -> list[ParaboxItemInfo]:
        option = cls.get_option(options)

        def create_items_unmodified():
            match option:
                case ShuffleProgressiveOrSeperateOptionValues.option_single:
                    return cls.get_items_single(options)
                case ShuffleProgressiveOrSeperateOptionValues.option_progressive:
                    return cls.get_items_progressive(options)
                case ShuffleProgressiveOrSeperateOptionValues.option_seperate:
                    return cls.get_items_seperate(options)
                case _:
                    return []

        return cls.modify_items(create_items_unmodified(), options)


class PriorityItemDataCreator(ParaboxShuffleItemDataCreator):
    @staticmethod
    def get_option(options: ParaboxOptionValues) -> int:
        return options.shuffle_priority

    items = [Items.priority]


class UndoItemDataCreator(ParaboxShuffleItemDataCreator):
    @staticmethod
    def get_option(options: ParaboxOptionValues) -> int:
        return options.shuffle_undo

    @staticmethod
    def get_undo_type(options: ParaboxOptionValues):
        if (
                options.shuffle_level_select != ShuffleLevelSelectValues.option_disabled
                and options.fix_banishment == FixBanishmentValues.option_vanilla
                and options.world_generation not in [WorldGenerationValues.option_vanilla,
                                                     WorldGenerationValues.option_shuffle]
                and options.level_generation == LevelGenerationValues.option_randomize
        ):
            return ParaboxItemType.PROGRESSION
        else:
            return ParaboxItemType.USEFUL

    items = [Items.progressive_undo] * 2

    @classmethod
    def modify_items(cls, item_list: list[ParaboxItemInfo], options: ParaboxOptionValues) -> list[ParaboxItemInfo]:
        if not item_list:
            return item_list
        undo_type = cls.get_undo_type(options)
        item_list = [item.typed(undo_type) for item in item_list]
        return item_list + [item_list[0]] * options.undo_extra_copy_count


class PossessItemDataCreator(ParaboxShuffleItemDataCreator):
    @staticmethod
    def get_option(options: ParaboxOptionValues) -> int:
        return options.shuffle_possess

    items = [Items.possess_box, Items.possess_wall]


if __name__ == '__main__':
    print("Test")
    testOptions = {
        "goal": 0,
        "goal_unlock": 0,
        "goal_unlock_world_count": 0,
        "level_generation": 2,
        "world_generation": 2,
        "world_door_keys": 0,
        "world_door_key_group_count": 0,
        "world_count": 0,

        # Shuffle Options
        "shuffle_priority": 2,
        "shuffle_extrude": 0,
        "shuffle_inner_push": 0,
        "shuffle_block": 0,
        "shuffle_level_select": 3,
        "shuffle_clone": 0,
        "shuffle_open": 0,
        "shuffle_even": 0,
        "shuffle_oblong": 0,
        "shuffle_one": 0,

        "shuffle_recursion": 0,
        "shuffle_flip": 0,
        "shuffle_friend": 0,
        "shuffle_infinite_exit_block": 0,
        "shuffle_infinite_enter_block": 0,
        "shuffle_player": 0,
        "shuffle_undo": 3,
        "undo_extra_copy_count": 1,

        "shuffle_box_sizes": 0,
        "shuffle_nested_goal": 0,
        "shuffle_possess": 2,

        # Box Options
        "box_types": 0,

        # Logic Options
        "fix_banishment": 0,

        # Extra Options
        "priority_order": 0,
        "max_friend_count": 0,
        "max_infinite_exit_level": 0,
        "max_infinite_enter_level": 0,
    }
    testOptionsDataclass = option_values_from_dict(testOptions)
    print([(item.name, item.item_type.name) for item in PossessItemDataCreator.create_items(testOptionsDataclass)])
