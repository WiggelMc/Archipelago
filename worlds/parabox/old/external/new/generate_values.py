import definitions_items
from definitions_base import OptionProvider
from generate_decorators import option_providers

is_initialized: bool = False


def init():
    global is_initialized
    if is_initialized:
        return
    is_initialized = True

    definitions_items.init()


def get_option_providers() -> list[type[OptionProvider]]:
    init()
    return option_providers
