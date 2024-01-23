from Options import Choice
from worlds.parabox.external.decorators.docstrings import inherit_docstring
from worlds.parabox.external.opt.box_option_values import BoxTypesValues


@inherit_docstring
class BoxTypes(BoxTypesValues, Choice):
    pass
