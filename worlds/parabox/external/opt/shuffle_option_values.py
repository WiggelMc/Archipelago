from .option_base_values import ShuffleOptionValues, ShuffleProgressiveOptionValues, \
    ShuffleProgressiveOrSeperateOptionValues


class ShufflePriorityValues(ShuffleOptionValues):
    """
    TODO: Option Description
    """
    display_name = "Shuffle Priority"


class ShuffleExtrudeValues(ShuffleOptionValues):
    """
    TODO: Option Description
    """
    display_name = "Shuffle Extrude"


class ShuffleInnerPushValues(ShuffleOptionValues):
    """
    TODO: Option Description
    """
    display_name = "Shuffle Inner Push"


class ShuffleBlockValues(ShuffleOptionValues):
    """
    TODO: Option Description
    """
    display_name = "Shuffle Block"


class ShuffleLevelSelectValues(ShuffleOptionValues):
    """
    TODO: Option Description
    """
    display_name = "Shuffle Level Select"


class ShuffleCloneValues(ShuffleOptionValues):
    """
    TODO: Option Description
    """
    display_name = "Shuffle Clone"


class ShuffleOpenValues(ShuffleOptionValues):
    """
    TODO: Option Description
    """
    display_name = "Shuffle Open"


class ShuffleEvenValues(ShuffleOptionValues):
    """
    TODO: Option Description
    """
    display_name = "Shuffle Even"


class ShuffleOblongValues(ShuffleOptionValues):
    """
    TODO: Option Description
    """
    display_name = "Shuffle Oblong"


class ShuffleOneValues(ShuffleOptionValues):
    """
    TODO: Option Description
    """
    display_name = "Shuffle One"


class ShuffleRecursionValues(ShuffleProgressiveOptionValues):
    """
    TODO: Option Description
    """
    display_name = "Shuffle Recursion"


class ShuffleFlipValues(ShuffleProgressiveOptionValues):
    """
    TODO: Option Description
    """
    display_name = "Shuffle Flip"


class ShuffleFriendValues(ShuffleProgressiveOptionValues):
    """
    TODO: Option Description
    """
    display_name = "Shuffle Friend"


class ShuffleInfiniteExitBlockValues(ShuffleProgressiveOptionValues):
    """
    TODO: Option Description
    """
    display_name = "Shuffle Infinite Exit Block"


class ShuffleInfiniteEnterBlockValues(ShuffleProgressiveOptionValues):
    """
    TODO: Option Description
    """
    display_name = "Shuffle Infinite Enter Block"


class ShufflePlayerValues(ShuffleProgressiveOptionValues):
    """
    TODO: Option Description
    """
    display_name = "Shuffle Player"


class ShuffleUndoValues(ShuffleProgressiveOptionValues):
    """
    TODO: Option Description
    """
    display_name = "Shuffle Undo"
    default = ShuffleProgressiveOptionValues.option_unlocked


class UndoExtraCopyCountValues:
    """
    TODO: Option Description
    """
    display_name = "Undo Extra Copy Count"
    range_start = 0
    range_end = 10
    default = 0


class ShuffleBoxSizesValues(ShuffleProgressiveOrSeperateOptionValues):
    """
    TODO: Option Description
    """
    display_name = "Shuffle Box Sizes"


class ShuffleNestedGoalValues(ShuffleProgressiveOrSeperateOptionValues):
    """
    TODO: Option Description
    """
    display_name = "Shuffle Nested Goal"


class ShufflePossessValues(ShuffleProgressiveOrSeperateOptionValues):
    """
    TODO: Option Description
    """
    display_name = "Shuffle Possess"
