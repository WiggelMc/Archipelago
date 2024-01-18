from Options import Choice


class ShuffleOption(Choice):
    option_disabled = 0
    option_unlocked = 1
    option_single = 2
    default = option_single


class ShuffleProgressiveOption(ShuffleOption):
    option_progressive = 3
    default = option_progressive


class ShuffleProgressiveOrSeperateOption(ShuffleProgressiveOption):
    option_seperate = 4
    default = super().option_progressive
