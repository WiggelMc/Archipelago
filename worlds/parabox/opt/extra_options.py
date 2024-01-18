from Options import Choice, Range


class PriorityOrder(Choice):
    """
    TODO: Option Description
    """
    display_name = "Priority Order"
    option_vanilla = 0
    option_random_level = 1
    option_random_seed = 2
    default = option_random_level


class MaxFriendCount(Range):
    """
    TODO: Option Description
    """
    display_name = "Max Friend Count"
    range_start = 1
    range_end = 20
    default = 4


class MaxInfiniteExitLevel(Range):
    """
    TODO: Option Description
    """
    display_name = "Max Infinite Exit Level"
    range_start = 1
    range_end = 10
    default = 5


class MaxInfiniteEnterLevel(Range):
    """
    TODO: Option Description
    """
    display_name = "Max Infinite Enter Level"
    range_start = 1
    range_end = 10
    default = 5
