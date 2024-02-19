import dataclasses
from dataclasses import dataclass
from typing import Any

from worlds.parabox.old.opt import shuffle_options
from worlds.parabox.old.opt import logic_options, extra_options, box_options, world_options
from Options import PerGameCommonOptions


@dataclass
class ParaboxOptions(PerGameCommonOptions):
    # World Options
    goal: world_options.Goal
    goal_unlock: world_options.GoalUnlock
    goal_unlock_world_count: world_options.GoalUnlockWorldCount
    level_generation: world_options.LevelGeneration
    world_generation: world_options.WorldGeneration
    world_door_keys: world_options.WorldDoorKeys
    world_door_key_group_count: world_options.WorldDoorKeyGroupCount
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
    undo_extra_copy_count: shuffle_options.UndoExtraCopyCount

    shuffle_box_sizes: shuffle_options.ShuffleBoxSizes
    shuffle_nested_goal: shuffle_options.ShuffleNestedGoal
    shuffle_possess: shuffle_options.ShufflePossess

    # Box Options
    box_types: box_options.BoxTypes

    # Logic Options
    fix_banishment: logic_options.FixBanishment

    # Extra Options
    priority_order: extra_options.PriorityOrder
    max_friend_count: extra_options.MaxFriendCount
    max_infinite_exit_level: extra_options.MaxInfiniteExitLevel
    max_infinite_enter_level: extra_options.MaxInfiniteEnterLevel


def options_to_dict(options: ParaboxOptions) -> dict[str, Any]:
    return options.as_dict(*[field.name for field in dataclasses.fields(ParaboxOptions)], casing="snake")