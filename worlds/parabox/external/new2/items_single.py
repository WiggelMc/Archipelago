import typing
from dataclasses import dataclass

from . import common_values
from .item_provider_base import PoolItem
from .items_base import StackedItemDefinition, SingleReqItem, generate_items
from .option_provider_base import EnumOptionValue
from .options_base import AutoEnumOption, generate_option
from .string_case_utils import to_case, NameCase


class SingleOptionValue(EnumOptionValue):
    Disabled = 0
    Unlocked = 1
    Single = 2


@dataclass(kw_only=True)
class SingleOption(AutoEnumOption):
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


def format_description(text: str):
    return f"""
        {text}
        {common_values.shuffle_option_disabled_description}
        {common_values.shuffle_option_unlocked_description}
        {common_values.shuffle_option_single_description}
    """


def generate_single_item_definition(cls: type[TSingleItemDefinition]) -> type[TSingleItemDefinition]:
    name_pascal = to_case(cls.__name__, NameCase.Pascal, NameCase.Pascal)
    opt_name_pascal = f"{common_values.shuffle_option_prefix_pascal}{name_pascal}"

    generate_option(cls.opt, opt_name_pascal, format_description)

    items = [cls.single]
    generate_items(items, name_pascal)
    cls.items = items

    return cls
