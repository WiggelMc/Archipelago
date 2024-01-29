from __future__ import annotations
from dataclasses import dataclass

from . import common_values
from .item_provider_base import PoolItem
from .items_base import StackedItemDefinition, SeperateReqItem, ProgressiveItem, SingleItem, generate_items
from .option_provider_base import EnumOptionValue
from .options_base import AutoEnumOption, generate_option
from .string_case_utils import to_case, NameCase


class SeperateOptionValue(EnumOptionValue):
    Disabled = 0
    Unlocked = 1
    Single = 2
    Progressive = 3
    Seperate = 4


@dataclass(kw_only=True)
class SeperateOption(AutoEnumOption):
    default: SeperateOptionValue
    description_text: str = None
    display_name: str = None
    description: str = None
    class_name: str = None
    key_name: str = None
    enum = SeperateOptionValue


def format_description(text: str):
    return f"""
        {text}
        {common_values.shuffle_option_disabled_description}
        {common_values.shuffle_option_unlocked_description}
        {common_values.shuffle_option_single_description}
        {common_values.shuffle_option_progressive_description}
        {common_values.shuffle_option_seperate_description}
    """


class SeperateItemDefinition(StackedItemDefinition):
    @classmethod
    def _generate(cls):
        name_pascal = to_case(cls.__name__, NameCase.Pascal, NameCase.Pascal)
        opt_name_pascal = f"{common_values.shuffle_option_prefix_pascal}{name_pascal}"

        generate_option(cls.opt, opt_name_pascal, format_description)

        seperate_prefix = "seperate_"
        seperate_items: dict[str, SeperateReqItem] = {
            k[len(seperate_prefix):]: v for k, v in cls.__dict__.items()
            if k.startswith(seperate_prefix) and k != "seperate_items"
        }
        seperate_items_list = list(seperate_items.values())

        if (not hasattr(cls, "progressive_amount")) or cls.progressive_amount is None:
            cls.progressive_amount = max((item.stage for item in seperate_items_list))

        items = [cls.single, cls.progressive] + seperate_items_list
        generate_items(items, name_pascal)
        cls.seperate_items = seperate_items
        cls.items = items
        super()._generate()

    @classmethod
    def pool_items(cls, options: dict[str, int]) -> list[PoolItem]:
        match cls.option(options):
            case SeperateOptionValue.Single:
                return [cls.single]
            case SeperateOptionValue.Progressive:
                return [cls.progressive] * cls.progressive_amount
            case SeperateOptionValue.Seperate:
                return list(cls.seperate_items.values())
        return []

    @classmethod
    def option(cls, options: dict[str, int]) -> SeperateOptionValue:
        return SeperateOptionValue(options[cls.opt.key_name])

    progressive_amount: int
    seperate_items: dict[str, SeperateReqItem]

    single: SingleItem
    progressive: ProgressiveItem
    opt: SeperateOption
