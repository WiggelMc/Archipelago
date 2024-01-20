from Options import Choice


class BoxTypesValues:
    option_single = 0
    option_no_mixing = 1
    option_mixing = 2
    default = option_mixing


class BoxTypes(BoxTypesValues, Choice):
    """
    TODO: Option Description
    """
    display_name = "Box Types"
