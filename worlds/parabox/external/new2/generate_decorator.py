import typing

from .items_single import SingleItemDefinition, generate_single_item_definition
from .option_provider_base import EnumOptionProvider, RangeOptionProvider

enum_option_providers: list[EnumOptionProvider] = []
range_option_providers: list[RangeOptionProvider] = []

TAny = typing.TypeVar("TAny")


def _generate_options(cls: type[TAny]):
    match cls:
        case EnumOptionProvider.__class__():
            enum_option_providers.append(cls())
        case RangeOptionProvider.__class__():
            range_option_providers.append(cls())


def _generate_items(cls: type[TAny]):
    pass


def _generate_class(cls: type[TAny]) -> type[TAny]:
    match cls:
        case SingleItemDefinition.__class__():
            return generate_single_item_definition(cls)
        case _:
            raise TypeError()


def generate(cls: type[TAny]) -> type[TAny]:
    cls = _generate_class(cls)
    _generate_options(cls)
    _generate_items(cls)
    return cls
