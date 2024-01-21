from Options import Choice, Range


class Goal(Choice):
    """
    TODO: Option Description
    """
    display_name = "Goal"
    option_button = 0
    option_level = 1
    option_challenge = 2
    default = option_button


class GoalUnlock(Choice):
    """
    TODO: Option Description
    """
    display_name = "Goal Unlock"
    option_reach = 0
    option_world_exits = 1
    option_world_completes = 2
    default = option_world_exits


class GoalUnlockWorldCount(Range):
    """
    TODO: Option Description
    """
    display_name = "Goal Unlock World Count"
    range_start = 1
    range_end = 100
    default = 10


class LevelGeneration(Choice):
    """
    TODO: Option Description
    """
    display_name = "Level Generation"
    option_vanilla = 0
    option_remix = 1
    option_randomize = 2
    default = option_vanilla


class WorldGeneration(Choice):
    """
    TODO: Option Description
    """
    display_name = "World Generation"
    option_vanilla = 0
    option_shuffle = 1
    option_random = 2
    default = option_vanilla


class WorldCount(Range):
    """
    TODO: Option Description
    """
    display_name = "World Count"
    range_start = 1
    range_end = 100
    default = 20
