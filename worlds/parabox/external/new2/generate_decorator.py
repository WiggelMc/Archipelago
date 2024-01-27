import typing

from items_single import SingleItemDefinition, generate_single_item_definition

TAny = typing.TypeVar("TAny")


def generate(cls: type[TAny]) -> type[TAny]:
    match cls:
        case SingleItemDefinition.__class__():
            return generate_single_item_definition(cls)
        case _:
            raise TypeError()
