from __future__ import annotations
from dataclasses import dataclass

from . import common_values
from .item_provider_base import PoolItem
from .items_base import StackedItemDefinition, SingleItem, ProgressiveReqItem, generate_items
from .option_provider_base import EnumOptionValue
from .options_base import AutoEnumOption, generate_option
from .string_case_utils import to_case, NameCase


class ProgressiveOptionValue(EnumOptionValue):
    Disabled = 0
    Unlocked = 1
    Single = 2
    Progressive = 3


@dataclass(kw_only=True)
class ProgressiveOption(AutoEnumOption):
    default: ProgressiveOptionValue
    description_text: str = None
    display_name: str = None
    description: str = None
    class_name: str = None
    key_name: str = None
    enum = ProgressiveOptionValue


def format_description(text: str):
    return f"""
        {text}
        {common_values.shuffle_option_disabled_description}
        {common_values.shuffle_option_unlocked_description}
        {common_values.shuffle_option_single_description}
        {common_values.shuffle_option_progressive_description}
    """


class ProgressiveItemDefinition(StackedItemDefinition):
    @classmethod
    def _generate(cls):
        name_pascal = to_case(cls.__name__, NameCase.Pascal, NameCase.Pascal)
        opt_name_pascal = f"{common_values.shuffle_option_prefix_pascal}{name_pascal}"

        generate_option(cls.opt, opt_name_pascal, format_description)

        items = [cls.single, cls.progressive]
        generate_items(items, name_pascal)
        cls.items = items
        super()._generate()

    @classmethod
    def pool_items(cls, options: dict[str, int]) -> list[PoolItem]:
        match cls.option(options):
            case ProgressiveOptionValue.Single:
                return [cls.single]
            case ProgressiveOptionValue.Progressive:
                return [cls.progressive] * cls.progressive_amount
        return []

    @classmethod
    def option(cls, options: dict[str, int]) -> ProgressiveOptionValue:
        return ProgressiveOptionValue(options[cls.opt.key_name])

    single: SingleItem
    progressive: ProgressiveReqItem
    progressive_amount: int
    opt: ProgressiveOption
