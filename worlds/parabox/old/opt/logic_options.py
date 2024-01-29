from Options import Choice
from worlds.parabox.old.external.decorators.docstrings import inherit_docstring
from worlds.parabox.external import FixBanishmentValues


@inherit_docstring
class FixBanishment(FixBanishmentValues, Choice):
    pass
