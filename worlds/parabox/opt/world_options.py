from Options import Choice, Range
from worlds.parabox.external.opt.world_option_values import GoalValues, GoalUnlockValues, GoalUnlockWorldCountValues, \
    LevelGenerationValues, WorldGenerationValues, WorldDoorKeysValues, WorldDoorKeyGroupCountValues, WorldCountValues, \
    WorldSelectionBiasValues


class Goal(GoalValues, Choice):
    __doc__ = GoalValues.__doc__


class GoalUnlock(GoalUnlockValues, Choice):
    __doc__ = GoalUnlockValues.__doc__


class GoalUnlockWorldCount(GoalUnlockWorldCountValues, Range):
    __doc__ = GoalUnlockWorldCountValues.__doc__


class LevelGeneration(LevelGenerationValues, Choice):
    __doc__ = LevelGenerationValues.__doc__


class WorldGeneration(WorldGenerationValues, Choice):
    __doc__ = WorldGenerationValues.__doc__


class WorldDoorKeys(WorldDoorKeysValues, Choice):
    __doc__ = WorldDoorKeysValues.__doc__


class WorldDoorKeyGroupCount(WorldDoorKeyGroupCountValues, Range):
    __doc__ = WorldDoorKeyGroupCountValues.__doc__


class WorldCount(WorldCountValues, Range):
    __doc__ = WorldCountValues.__doc__


class WorldSelectionBias(WorldSelectionBiasValues, Range):
    __doc__ = WorldSelectionBiasValues.__doc__
