from Options import Choice


class ShuffleOption(Choice):
    option_disabled = 0
    option_unlocked = 1
    option_single = 2
    default = 2


class ShuffleProgressiveOption(ShuffleOption):
    option_progressive = 3
    default = 3


class ShuffleProgressiveOrSeperateOption(ShuffleProgressiveOption):
    option_seperate = 4
    default = 3
