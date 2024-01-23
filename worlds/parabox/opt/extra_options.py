from Options import Choice, Range
from worlds.parabox.external.decorators.docstrings import inherit_docstring
from worlds.parabox.external.opt.extra_option_values import PriorityOrderValues, MaxFriendCountValues, \
    MaxInfiniteExitLevelValues, MaxInfiniteEnterLevelValues


@inherit_docstring
class PriorityOrder(PriorityOrderValues, Choice):
    pass


@inherit_docstring
class MaxFriendCount(MaxFriendCountValues, Range):
    pass


@inherit_docstring
class MaxInfiniteExitLevel(MaxInfiniteExitLevelValues, Range):
    pass


@inherit_docstring
class MaxInfiniteEnterLevel(MaxInfiniteEnterLevelValues, Range):
    pass
