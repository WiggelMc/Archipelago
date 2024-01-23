class GoalValues:
    """
    TODO: Option Description
    """
    display_name = "Goal"
    option_button = 0
    option_level = 1
    option_challenge = 2
    default = option_button


class GoalUnlockValues:
    """
    TODO: Option Description
    """
    display_name = "Goal Unlock"
    option_reach = 0
    option_world_exits = 1
    option_world_completes = 2
    default = option_world_exits


class GoalUnlockWorldCountValues:
    """
    TODO: Option Description
    """
    display_name = "Goal Unlock World Count"
    range_start = 1
    range_end = 100
    default = 10


class LevelGenerationValues:
    """
    TODO: Option Description
    """
    display_name = "Level Generation"
    option_vanilla = 0
    option_remix = 1
    option_randomize = 2
    default = option_vanilla


class WorldGenerationValues:
    """
    TODO: Option Description
    """
    display_name = "World Generation"
    option_vanilla = 0
    option_shuffle = 1
    option_random = 2
    default = option_vanilla


class WorldDoorKeysValues:
    """
    TODO: Option Description
    """
    display_name = "World Door Keys"
    option_levels = 0
    option_keys = 1
    option_mixed = 2
    default = option_levels


class WorldDoorKeyGroupCountValues:
    """
    TODO: Option Description
    """
    display_name = "World Door Key Group Count"
    range_start = 1
    range_end = 100
    default = 100


class WorldCountValues:
    """
    TODO: Option Description
    """
    display_name = "World Count"
    range_start = 1
    range_end = 100
    default = 20


class WorldSelectionBiasValues:
    """
    TODO: Option Description
    """
    display_name = "World Selection Bias"
    range_start = 1
    range_end = 100
    default = 70
