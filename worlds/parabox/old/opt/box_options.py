from Options import Choice
from worlds.parabox.old.external.decorators.docstrings import inherit_docstring
from worlds.parabox.external import BoxTypesValues


@inherit_docstring
class BoxTypes(BoxTypesValues, Choice):
    pass
