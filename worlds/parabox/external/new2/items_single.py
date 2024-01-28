import typing
from dataclasses import dataclass

from . import common_values
from .item_provider_base import PoolItem
from .items_base import StackedItemDefinition, SingleReqItem
from .option_provider_base import EnumOption, EnumOptionValue
from .string_case_utils import to_case, NameCase


class SingleOptionValue(EnumOptionValue):
    Disabled = 0
    Unlocked = 1
    Single = 2


@dataclass(kw_only=True)
class SingleOption(EnumOption):
    default: SingleOptionValue
    description_text: str = None
    display_name: str = None
    description: str = None
    class_name: str = None
    key_name: str = None


class SingleItemDefinition(StackedItemDefinition):
    @classmethod
    def pool_items(cls, options: dict[str, int]) -> list[PoolItem]:
        match cls.option(options):
            case SingleOptionValue.Single:
                return [cls.single]
        return []

    @classmethod
    def option(cls, options: dict[str, int]) -> SingleOptionValue:
        return SingleOptionValue(options[cls.opt.key_name])

    single: SingleReqItem
    opt: SingleOption


TSingleItemDefinition = typing.TypeVar("TSingleItemDefinition", bound=SingleItemDefinition)


def remove_whitespace(text: str):
    return "\n".join(
        (line for line in (line.strip() for line in text.split("\n")) if line)
    )


def format_description(text: str):
    return f"""
        {text}
        {common_values.shuffle_option_disabled_description}
        {common_values.shuffle_option_unlocked_description}
        {common_values.shuffle_option_single_description}
    """


def generate_single_item_definition(cls: type[TSingleItemDefinition]) -> type[TSingleItemDefinition]:
    name_pascal = to_case(cls.__name__, NameCase.Pascal, NameCase.Pascal)
    name_word = to_case(name_pascal, NameCase.Pascal, NameCase.WordTitle)
    opt_name_pascal = f"{common_values.shuffle_option_prefix_pascal}{name_pascal}"
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

    single = cls.single
    if (single.id is None) and (single.id_offset is not None):
        single.id = single.id_offset + common_values.item_base_id
    if not single.name:
        single.name = name_word
    cls.items = [cls.single]

    return cls
