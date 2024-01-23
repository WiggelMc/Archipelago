from Options import Choice, Range
from worlds.parabox.external.decorators.docstrings import inherit_docstring
from worlds.parabox.external.opt.shuffle_option_values import ShufflePriorityValues, ShuffleExtrudeValues, \
    ShuffleInnerPushValues, ShuffleBlockValues, ShuffleLevelSelectValues, ShuffleCloneValues, ShuffleOpenValues, \
    ShuffleEvenValues, ShuffleOblongValues, ShuffleOneValues, ShuffleRecursionValues, ShuffleFlipValues, \
    ShuffleFriendValues, ShuffleInfiniteExitBlockValues, ShuffleInfiniteEnterBlockValues, ShufflePlayerValues, \
    ShuffleUndoValues, UndoExtraCopyCountValues, ShuffleBoxSizesValues, ShuffleNestedGoalValues, ShufflePossessValues


@inherit_docstring
class ShufflePriority(ShufflePriorityValues, Choice):
    pass


@inherit_docstring
class ShuffleExtrude(ShuffleExtrudeValues, Choice):
    pass


@inherit_docstring
class ShuffleInnerPush(ShuffleInnerPushValues, Choice):
    pass


@inherit_docstring
class ShuffleBlock(ShuffleBlockValues, Choice):
    pass


@inherit_docstring
class ShuffleLevelSelect(ShuffleLevelSelectValues, Choice):
    pass


@inherit_docstring
class ShuffleClone(ShuffleCloneValues, Choice):
    pass


@inherit_docstring
class ShuffleOpen(ShuffleOpenValues, Choice):
    pass


@inherit_docstring
class ShuffleEven(ShuffleEvenValues, Choice):
    pass


@inherit_docstring
class ShuffleOblong(ShuffleOblongValues, Choice):
    pass


@inherit_docstring
class ShuffleOne(ShuffleOneValues, Choice):
    pass


@inherit_docstring
class ShuffleRecursion(ShuffleRecursionValues, Choice):
    pass


@inherit_docstring
class ShuffleFlip(ShuffleFlipValues, Choice):
    pass


@inherit_docstring
class ShuffleFriend(ShuffleFriendValues, Choice):
    pass


@inherit_docstring
class ShuffleInfiniteExitBlock(ShuffleInfiniteExitBlockValues, Choice):
    pass


@inherit_docstring
class ShuffleInfiniteEnterBlock(ShuffleInfiniteEnterBlockValues, Choice):
    pass


@inherit_docstring
class ShufflePlayer(ShufflePlayerValues, Choice):
    pass


@inherit_docstring
class ShuffleUndo(ShuffleUndoValues, Choice):
    pass


@inherit_docstring
class UndoExtraCopyCount(UndoExtraCopyCountValues, Range):
    pass


@inherit_docstring
class ShuffleBoxSizes(ShuffleBoxSizesValues, Choice):
    pass


@inherit_docstring
class ShuffleNestedGoal(ShuffleNestedGoalValues, Choice):
    pass


@inherit_docstring
class ShufflePossess(ShufflePossessValues, Choice):
    pass
