import typing
from dataclasses import dataclass

from items_base import StackedItemDefinition
from option_provider_base import Option, OptionValue
from string_case_utils import to_case, NameCase


class SingleOptionValue(OptionValue):
    Disabled = 0
    Unlocked = 1
    Single = 2


@dataclass
class SingleOption(Option):
    default: SingleOptionValue
    description_text: str = None
    display_name: str = None
    description: str = None
    class_name: str = None
    key_name: str = None


class SingleItemDefinition(StackedItemDefinition):
    @classmethod
    def option(cls, options: dict[str, int]) -> SingleOptionValue:
        return SingleOptionValue(options[cls.opt.key_name])

    opt: SingleOption
    single: typing.Any


TSingleItemDefinition = typing.TypeVar("TSingleItemDefinition", bound=SingleItemDefinition)


def remove_whitespace(text: str):
    return "\n".join(
        (line for line in (line.strip() for line in text.split("\n")) if line)
    )


def format_description(text: str):
    return f"""
        {text}
        Disabled: Element will not be present in the game
        Unlocked: Element will be unlocked immediatly 
        Single: Element will be shuffled as a Single Item
    """


def generate_single_item_definition(cls: type[TSingleItemDefinition]) -> type[TSingleItemDefinition]:
    name_snake = to_case(cls.__name__, NameCase.Pascal, NameCase.Snake)
    name_word = to_case(cls.__name__, NameCase.Pascal, NameCase.WordTitle)
    name_pascal = cls.__name__

    opt = cls.opt
    if not opt.key_name:
        opt.key_name = f"shuffle_{name_snake}"
    if not opt.class_name:
        opt.class_name = f"Shuffle{name_pascal}"
    if not opt.display_name:
        opt.display_name = f"Shuffle {name_word}"
    if (not opt.description) and opt.description_text:
        opt.description = format_description(opt.description_text)
    opt.description = remove_whitespace(opt.description)

    return cls
