import typing

from . import common_values
from .string_format_utils import remove_whitespace
from .option_provider_base import EnumOption, Option
from .string_case_utils import to_case, NameCase


class AutoOption(Option):
    description_text: str


class AutoEnumOption(EnumOption, AutoOption):
    pass


def generate_option(opt: AutoOption, name_pascal: str, description_formatter: typing.Callable[[str], str]):
    opt_name_pascal = f"{common_values.shuffle_option_prefix_pascal}{name_pascal}"
    opt_name_snake = to_case(opt_name_pascal, NameCase.Pascal, NameCase.Snake)
    opt_name_word = to_case(opt_name_pascal, NameCase.Pascal, NameCase.WordTitle)

    if not opt.key_name:
        opt.key_name = opt_name_snake
    if not opt.class_name:
        opt.class_name = opt_name_pascal
    if not opt.display_name:
        opt.display_name = opt_name_word
    if (not opt.description) and opt.description_text:
        opt.description = description_formatter(opt.description_text)
    opt.description = remove_whitespace(opt.description)
