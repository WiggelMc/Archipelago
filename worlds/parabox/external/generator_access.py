from . import d_items_single, d_items_progressive, d_items_seperate, d_items_trap, d_items_useful
from .item_provider_base import item_providers
from .option_provider_base import enum_option_providers, range_option_providers, option_providers


class _GeneratorAccessor:
    def __new__(cls):
        d_items_single.init()
        d_items_progressive.init()
        d_items_seperate.init()
        d_items_trap.init()
        d_items_useful.init()
        return super().__new__(cls)

    @property
    def item_providers(self):
        return item_providers

    @property
    def option_providers(self):
        return option_providers

    @property
    def enum_option_providers(self):
        return enum_option_providers

    @property
    def range_option_providers(self):
        return range_option_providers


GeneratorAccessor = _GeneratorAccessor()
