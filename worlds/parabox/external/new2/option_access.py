from .generate_decorator import enum_option_providers
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


def get_option_providers():
    init()
    return enum_option_providers
