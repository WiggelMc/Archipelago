import typing

from .items_single import SingleItemDefinition, generate_single_item_definition
from .option_provider_base import OptionProvider


option_providers: list[OptionProvider] = []

TAny = typing.TypeVar("TAny")


def generate(cls: type[TAny]) -> type[TAny]:
    match cls:
        case OptionProvider.__class__():
            option_providers.append(cls())
    match cls:
        case SingleItemDefinition.__class__():
            return generate_single_item_definition(cls)
        case _:
            raise TypeError()
