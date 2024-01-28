from .generate_decorator import enum_option_providers, range_option_providers, item_providers
from . import d_items_single

initialized = False


def _init():
    d_items_single.init()


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
