from items_base import ParaboxSingleItemInfo, ProgressiveItemInfoGroup, ParaboxProgressiveItemInfo, \
    SeperateItemInfoGroup, ParaboxSeperateItemInfo, SingleItemInfoGroup
from option_values import ParaboxOptionValues


class Priority(SingleItemInfoGroup):
    @classmethod
    def get_option(cls, options: ParaboxOptionValues) -> int:
        return options.shuffle_priority

    single = ParaboxSingleItemInfo("Priority", 1)


class Extrude(SingleItemInfoGroup):
    @classmethod
    def get_option(cls, options: ParaboxOptionValues) -> int:
        return options.shuffle_extrude

    single = ParaboxSingleItemInfo("Extrude", 2)


class InnerPush(SingleItemInfoGroup):
    @classmethod
    def get_option(cls, options: ParaboxOptionValues) -> int:
        return options.shuffle_inner_push

    single = ParaboxSingleItemInfo("Inner Push", 3)


class Block(SingleItemInfoGroup):
    @classmethod
    def get_option(cls, options: ParaboxOptionValues) -> int:
        return options.shuffle_block

    single = ParaboxSingleItemInfo("Block", 4)


class LevelSelect(SingleItemInfoGroup):
    @classmethod
    def get_option(cls, options: ParaboxOptionValues) -> int:
        return options.shuffle_level_select

    single = ParaboxSingleItemInfo("Level Select", 5)


class Clone(SingleItemInfoGroup):
    @classmethod
    def get_option(cls, options: ParaboxOptionValues) -> int:
        return options.shuffle_clone

    single = ParaboxSingleItemInfo("Clone", 6)


class Open(SingleItemInfoGroup):
    @classmethod
    def get_option(cls, options: ParaboxOptionValues) -> int:
        return options.shuffle_open

    single = ParaboxSingleItemInfo("Open", 7)


class Even(SingleItemInfoGroup):
    @classmethod
    def get_option(cls, options: ParaboxOptionValues) -> int:
        return options.shuffle_even

    single = ParaboxSingleItemInfo("Even", 8)


class Oblong(SingleItemInfoGroup):
    @classmethod
    def get_option(cls, options: ParaboxOptionValues) -> int:
        return options.shuffle_oblong

    single = ParaboxSingleItemInfo("Oblong", 9)


class One(SingleItemInfoGroup):
    @classmethod
    def get_option(cls, options: ParaboxOptionValues) -> int:
        return options.shuffle_one

    single = ParaboxSingleItemInfo("One", 10)


class Recursion(ProgressiveItemInfoGroup):
    @classmethod
    def get_option(cls, options: ParaboxOptionValues) -> int:
        return options.shuffle_recursion

    single = ParaboxSingleItemInfo("Recursion", 11)
    progressive = ParaboxProgressiveItemInfo("Progressive Recursion", 12)


class Flip(ProgressiveItemInfoGroup):
    @classmethod
    def get_option(cls, options: ParaboxOptionValues) -> int:
        return options.shuffle_flip

    single = ParaboxSingleItemInfo("Flip", 13)
    progressive = ParaboxProgressiveItemInfo("Progressive Flip", 14)


class Friend(ProgressiveItemInfoGroup):
    @classmethod
    def get_option(cls, options: ParaboxOptionValues) -> int:
        return options.shuffle_friend

    single = ParaboxSingleItemInfo("Friend", 15)
    progressive = ParaboxProgressiveItemInfo("Progressive Friend", 16)


class InfiniteExitBlock(ProgressiveItemInfoGroup):
    @classmethod
    def get_option(cls, options: ParaboxOptionValues) -> int:
        return options.shuffle_infinite_exit_block

    single = ParaboxSingleItemInfo("Infinite Exit", 17)
    progressive = ParaboxProgressiveItemInfo("Progressive Infinite Exit", 18)


class InfiniteEnterBlock(ProgressiveItemInfoGroup):
    @classmethod
    def get_option(cls, options: ParaboxOptionValues) -> int:
        return options.shuffle_infinite_enter_block

    single = ParaboxSingleItemInfo("Infinite Enter", 19)
    progressive = ParaboxProgressiveItemInfo("Progressive Infinite Enter", 20)


class Player(ProgressiveItemInfoGroup):
    @classmethod
    def get_option(cls, options: ParaboxOptionValues) -> int:
        return options.shuffle_player

    single = ParaboxSingleItemInfo("Player", 21)
    progressive = ParaboxProgressiveItemInfo("Progressive Player", 22)


class Undo(ProgressiveItemInfoGroup):
    @classmethod
    def get_option(cls, options: ParaboxOptionValues) -> int:
        return options.shuffle_undo

    single = ParaboxSingleItemInfo("Undo", 23)
    progressive = ParaboxProgressiveItemInfo("Progressive Undo", 24)


class Possess(SeperateItemInfoGroup):
    @classmethod
    def get_option(cls, options: ParaboxOptionValues) -> int:
        return options.shuffle_possess

    single = ParaboxSingleItemInfo("Possess", 25)
    progressive = ParaboxProgressiveItemInfo("Progressive Possess", 26)
    seperate_wall = ParaboxSeperateItemInfo("Possess Wall", 27, n=1)
    seperate_box = ParaboxSeperateItemInfo("Possess Box", 28, n=2)


class NestedButton(SeperateItemInfoGroup):
    @classmethod
    def get_option(cls, options: ParaboxOptionValues) -> int:
        return options.shuffle_nested_goal

    single = ParaboxSingleItemInfo("Nested Button", 29)
    progressive = ParaboxProgressiveItemInfo("Progressive Nested Button", 30)
    seperate_box = ParaboxSeperateItemInfo("Nested Box Button", 31, n=1)
    seperate_player = ParaboxSeperateItemInfo("Nested Player Button", 32, n=2)
