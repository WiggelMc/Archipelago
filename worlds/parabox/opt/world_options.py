from Options import Choice, Range


class LevelGeneration(Choice):
    """
    TODO: Option Description
    """
    display_name = "Level Generation"
    option_vanilla = 0
    option_remix = 1
    option_randomize = 2
    default = 0


class WorldGeneration(Choice):
    """
    TODO: Option Description
    """
    display_name = "World Generation"
    option_normal = 0
    option_random = 1
    default = 0


class LevelCountOption(Range):
    range_start = 10
    range_end = 10000
    default = 100


class NormalLevelCount(LevelCountOption):
    """
    TODO: Option Description
    """
    display_name = "Normal Level Count"


class ChallengeLevelCount(LevelCountOption):
    """
    TODO: Option Description
    """
    display_name = "Challenge Level Count"


class WorldCount(Range):
    """
    TODO: Option Description
    """
    display_name = "World Count"
    range_start = 1
    range_end = 100
    default = 8
