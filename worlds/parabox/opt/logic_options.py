from Options import Choice
from worlds.parabox.external.decorators.docstrings import inherit_docstring
from worlds.parabox.external.opt.logic_option_values import FixBanishmentValues


@inherit_docstring
class FixBanishment(FixBanishmentValues, Choice):
    pass
