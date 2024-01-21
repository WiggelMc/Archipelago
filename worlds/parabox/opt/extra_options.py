from Options import Choice, Range
from worlds.parabox.external.opt.extra_option_values import PriorityOrderValues, MaxFriendCountValues, \
    MaxInfiniteExitLevelValues, MaxInfiniteEnterLevelValues


class PriorityOrder(PriorityOrderValues, Choice):
    __doc__ = PriorityOrderValues.__doc__


class MaxFriendCount(MaxFriendCountValues, Range):
    __doc__ = MaxFriendCountValues.__doc__


class MaxInfiniteExitLevel(MaxInfiniteExitLevelValues, Range):
    __doc__ = MaxInfiniteExitLevelValues.__doc__


class MaxInfiniteEnterLevel(MaxInfiniteEnterLevelValues, Range):
    __doc__ = MaxInfiniteEnterLevelValues.__doc__
