import typing

from .item_provider_base import ItemProvider
from .items_progressive import ProgressiveItemDefinition, generate_progressive_item_definition
from .items_seperate import SeperateItemDefinition, generate_seperate_item_definition
from .items_single import SingleItemDefinition, generate_single_item_definition
from .option_provider_base import EnumOptionProvider, RangeOptionProvider

enum_option_providers: list[EnumOptionProvider] = []
range_option_providers: list[RangeOptionProvider] = []
item_providers: list[ItemProvider] = []

TAny = typing.TypeVar("TAny")


def _generate_options(cls: type[TAny]):
    if issubclass(cls, EnumOptionProvider):
        enum_option_providers.append(cls())
    elif issubclass(cls, RangeOptionProvider):
        range_option_providers.append(cls())


def _generate_items(cls: type[TAny]):
    if issubclass(cls, ItemProvider):
        item_providers.append(cls())


def _generate_class(cls: type[TAny]) -> type[TAny]:
    if issubclass(cls, SingleItemDefinition):
        return generate_single_item_definition(cls)
    if issubclass(cls, ProgressiveItemDefinition):
        return generate_progressive_item_definition(cls)
    if issubclass(cls, SeperateItemDefinition):
        return generate_seperate_item_definition(cls)
    return cls


def generate(cls: type[TAny]) -> type[TAny]:
    cls = _generate_class(cls)
    _generate_options(cls)
    _generate_items(cls)
    return cls
