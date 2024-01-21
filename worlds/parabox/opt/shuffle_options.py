from Options import Choice, Range
from worlds.parabox.external.opt.shuffle_option_values import ShufflePriorityValues, ShuffleExtrudeValues, \
    ShuffleInnerPushValues, ShuffleBlockValues, ShuffleLevelSelectValues, ShuffleCloneValues, ShuffleOpenValues, \
    ShuffleEvenValues, ShuffleOblongValues, ShuffleOneValues, ShuffleRecursionValues, ShuffleFlipValues, \
    ShuffleFriendValues, ShuffleInfiniteExitBlockValues, ShuffleInfiniteEnterBlockValues, ShufflePlayerValues, \
    ShuffleUndoValues, UndoExtraCopyCountValues, ShuffleBoxSizesValues, ShuffleNestedGoalValues, ShufflePossessValues


# noinspection DuplicatedCode
class ShufflePriority(ShufflePriorityValues, Choice):
    __doc__ = ShufflePriorityValues.__doc__


class ShuffleExtrude(ShuffleExtrudeValues, Choice):
    __doc__ = ShuffleExtrudeValues.__doc__


class ShuffleInnerPush(ShuffleInnerPushValues, Choice):
    __doc__ = ShuffleInnerPushValues.__doc__


class ShuffleBlock(ShuffleBlockValues, Choice):
    __doc__ = ShuffleBlockValues.__doc__


class ShuffleLevelSelect(ShuffleLevelSelectValues, Choice):
    __doc__ = ShuffleLevelSelectValues.__doc__


class ShuffleClone(ShuffleCloneValues, Choice):
    __doc__ = ShuffleCloneValues.__doc__


class ShuffleOpen(ShuffleOpenValues, Choice):
    __doc__ = ShuffleOpenValues.__doc__


class ShuffleEven(ShuffleEvenValues, Choice):
    __doc__ = ShuffleEvenValues.__doc__


class ShuffleOblong(ShuffleOblongValues, Choice):
    __doc__ = ShuffleOblongValues.__doc__


class ShuffleOne(ShuffleOneValues, Choice):
    __doc__ = ShuffleOneValues.__doc__


# noinspection DuplicatedCode
class ShuffleRecursion(ShuffleRecursionValues, Choice):
    __doc__ = ShuffleRecursionValues.__doc__


class ShuffleFlip(ShuffleFlipValues, Choice):
    __doc__ = ShuffleFlipValues.__doc__


class ShuffleFriend(ShuffleFriendValues, Choice):
    __doc__ = ShuffleFriendValues.__doc__


class ShuffleInfiniteExitBlock(ShuffleInfiniteExitBlockValues, Choice):
    __doc__ = ShuffleInfiniteExitBlockValues.__doc__


class ShuffleInfiniteEnterBlock(ShuffleInfiniteEnterBlockValues, Choice):
    __doc__ = ShuffleInfiniteEnterBlockValues.__doc__


class ShufflePlayer(ShufflePlayerValues, Choice):
    __doc__ = ShufflePlayerValues.__doc__


class ShuffleUndo(ShuffleUndoValues, Choice):
    __doc__ = ShuffleUndoValues.__doc__


class UndoExtraCopyCount(UndoExtraCopyCountValues, Range):
    __doc__ = UndoExtraCopyCountValues.__doc__


class ShuffleBoxSizes(ShuffleBoxSizesValues, Choice):
    __doc__ = ShuffleBoxSizesValues.__doc__


class ShuffleNestedGoal(ShuffleNestedGoalValues, Choice):
    __doc__ = ShuffleNestedGoalValues.__doc__


class ShufflePossess(ShufflePossessValues, Choice):
    __doc__ = ShufflePossessValues.__doc__
