from dataclasses import dataclass


@dataclass
class ParaboxOptionsValues:
    # World Options
    goal: int
    goal_unlock: int
    goal_unlock_world_count: int
    level_generation: int
    world_generation: int
    world_door_keys: int
    world_door_key_group_count: int
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
    undo_extra_copy_count: int

    shuffle_box_sizes: int
    shuffle_nested_goal: int
    shuffle_possess: int

    # Box Options
    box_types: int

    # Logic Options
    fix_banishment: int

    # Extra Options
    priority_order: int
    max_friend_count: int
    max_infinite_exit_level: int
    max_infinite_enter_level: int
