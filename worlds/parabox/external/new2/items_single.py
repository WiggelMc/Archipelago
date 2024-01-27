import typing
from dataclasses import dataclass

import common_text
from items_base import StackedItemDefinition
from option_provider_base import Option, OptionValue
from string_case_utils import to_case, NameCase


class SingleOptionValue(OptionValue):
    Disabled = 0
    Unlocked = 1
    Single = 2


@dataclass(kw_only=True)
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
        {common_text.shuffle_option_disabled_description}
        {common_text.shuffle_option_unlocked_description}
        {common_text.shuffle_option_single_description}
    """


def generate_single_item_definition(cls: type[TSingleItemDefinition]) -> type[TSingleItemDefinition]:
    name_pascal = to_case(cls.__name__, NameCase.Pascal, NameCase.Pascal)
    opt_name_pascal = f"{common_text.shuffle_option_prefix_pascal}{name_pascal}"
    opt_name_snake = to_case(opt_name_pascal, NameCase.Pascal, NameCase.Snake)
    opt_name_word = to_case(opt_name_pascal, NameCase.Pascal, NameCase.WordTitle)

    opt = cls.opt
    if not opt.key_name:
        opt.key_name = opt_name_snake
    if not opt.class_name:
        opt.class_name = opt_name_pascal
    if not opt.display_name:
        opt.display_name = opt_name_word
    if (not opt.description) and opt.description_text:
        opt.description = format_description(opt.description_text)
    opt.description = remove_whitespace(opt.description)

    return cls
