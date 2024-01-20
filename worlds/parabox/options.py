from dataclasses import dataclass

from worlds.parabox.opt import world_options, shuffle_options, box_options, extra_options
from Options import PerGameCommonOptions


@dataclass
class ParaboxOptionsValues:
    level_generation: int
    world_generation: int
    normal_level_count: int
    challenge_level_count: int
    world_count: int

    # Shuffle Options
    shuffle_priority: int
    shuffle_extrude: int
    shuffle_inner_push: int
    shuffle_block: int
    shuffle_level_select: int
    shuffle_clone: int
    shuffle_open: int
    shuffle_even: int
    shuffle_oblong: int
    shuffle_one: int

    shuffle_recursion: int
    shuffle_flip: int
    shuffle_friend: int
    shuffle_infinite_exit_block: int
    shuffle_infinite_enter_block: int
    shuffle_player: int
    shuffle_undo: int

    shuffle_box_sizes: int
    shuffle_nested_goal: int
    shuffle_possess: int

    # Box Options
    box_types: int

    # Extra Options
    priority_order: int
    max_friend_count: int
    max_infinite_exit_level: int
    max_infinite_enter_level: int


@dataclass
class ParaboxOptions(PerGameCommonOptions):
    # World Options
    level_generation: world_options.LevelGeneration
    world_generation: world_options.WorldGeneration
    normal_level_count: world_options.NormalLevelCount
    challenge_level_count: world_options.ChallengeLevelCount
    world_count: world_options.WorldCount

    # Shuffle Options
    shuffle_priority: shuffle_options.ShufflePriority
    shuffle_extrude: shuffle_options.ShuffleExtrude
    shuffle_inner_push: shuffle_options.ShuffleInnerPush
    shuffle_block: shuffle_options.ShuffleBlock
    shuffle_level_select: shuffle_options.ShuffleLevelSelect
    shuffle_clone: shuffle_options.ShuffleClone
    shuffle_open: shuffle_options.ShuffleOpen
    shuffle_even: shuffle_options.ShuffleEven
    shuffle_oblong: shuffle_options.ShuffleOblong
    shuffle_one: shuffle_options.ShuffleOne

    shuffle_recursion: shuffle_options.ShuffleRecursion
    shuffle_flip: shuffle_options.ShuffleFlip
    shuffle_friend: shuffle_options.ShuffleFriend
    shuffle_infinite_exit_block: shuffle_options.ShuffleInfiniteExitBlock
    shuffle_infinite_enter_block: shuffle_options.ShuffleInfiniteEnterBlock
    shuffle_player: shuffle_options.ShufflePlayer
    shuffle_undo: shuffle_options.ShuffleUndo

    shuffle_box_sizes: shuffle_options.ShuffleBoxSizes
    shuffle_nested_goal: shuffle_options.ShuffleNestedGoal
    shuffle_possess: shuffle_options.ShufflePossess

    # Box Options
    box_types: box_options.BoxTypes

    # Extra Options
    priority_order: extra_options.PriorityOrder
    max_friend_count: extra_options.MaxFriendCount
    max_infinite_exit_level: extra_options.MaxInfiniteExitLevel
    max_infinite_enter_level: extra_options.MaxInfiniteEnterLevel
