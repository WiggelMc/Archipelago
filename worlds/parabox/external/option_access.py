from .generate_decorator import enum_option_providers, range_option_providers, item_providers
from . import d_items_single, d_items_progressive, d_items_seperate, d_items_trap, d_items_useful

initialized = False


def _init():
    d_items_single.init()
    d_items_progressive.init()
    d_items_seperate.init()
    d_items_trap.init()
    d_items_useful.init()


def init():
    global initialized
    if initialized:
        return
    initialized = True
    _init()


def get_enum_option_providers():
    init()
    return enum_option_providers


def get_range_option_providers():
    init()
    return range_option_providers


def get_item_providers():
    init()
    return item_providers
