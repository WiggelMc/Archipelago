from Options import Choice


class BoxTypes(Choice):
    """
    TODO: Option Description
    """
    display_name = "Box Types"
    option_single = 0
    option_no_mixing = 1
    option_mixing = 2
    default = option_mixing
