class ShuffleOptionValues:
    option_disabled = 0
    option_unlocked = 1
    option_single = 2
    default = option_single


class ShuffleProgressiveOptionValues(ShuffleOptionValues):
    option_progressive = 3
    default = option_progressive


class ShuffleProgressiveOrSeperateOptionValues(ShuffleProgressiveOptionValues):
    option_seperate = 4
    default = ShuffleProgressiveOptionValues.option_progressive
