from Options import Choice, Range
from worlds.parabox.external.decorators.docstrings import inherit_docstring
from worlds.parabox.external.opt.world_option_values import GoalValues, GoalUnlockValues, GoalUnlockWorldCountValues, \
    LevelGenerationValues, WorldGenerationValues, WorldDoorKeysValues, WorldDoorKeyGroupCountValues, WorldCountValues, \
    WorldSelectionBiasValues


@inherit_docstring
class Goal(GoalValues, Choice):
    pass


@inherit_docstring
class GoalUnlock(GoalUnlockValues, Choice):
    pass


@inherit_docstring
class GoalUnlockWorldCount(GoalUnlockWorldCountValues, Range):
    pass


@inherit_docstring
class LevelGeneration(LevelGenerationValues, Choice):
    pass


@inherit_docstring
class WorldGeneration(WorldGenerationValues, Choice):
    pass


@inherit_docstring
class WorldDoorKeys(WorldDoorKeysValues, Choice):
    pass


@inherit_docstring
class WorldDoorKeyGroupCount(WorldDoorKeyGroupCountValues, Range):
    pass


@inherit_docstring
class WorldCount(WorldCountValues, Range):
    pass


@inherit_docstring
class WorldSelectionBias(WorldSelectionBiasValues, Range):
    pass
