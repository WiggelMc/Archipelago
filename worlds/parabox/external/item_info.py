from __future__ import annotations

import abc
import dataclasses
import functools
from abc import abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Any

from option_values import ParaboxOptionValues


class ParaboxItemType(Enum):
    PROGRESSION = 1
    USEFUL = 2
    TRAP = 3


class ParaboxItemGroup(Enum):
    pass


@dataclass(frozen=True)
class ParaboxItemInfo:
    name: str
    id: int
    item_type: ParaboxItemType = ParaboxItemType.PROGRESSION

    def typed(self, item_type: ParaboxItemType):
        return dataclasses.replace(self, item_type=item_type)


@dataclass(frozen=True)
class ParaboxSingleItemInfo(ParaboxItemInfo):
    pass


@dataclass(frozen=True)
class ParaboxProgressiveItemInfo(ParaboxItemInfo):
    single_item: ParaboxSingleItemInfo = dataclasses.field(kw_only=True, default=None)


@dataclass(frozen=True)
class ParaboxSeperateItemInfo(ParaboxItemInfo):
    progressive_item: ParaboxProgressiveItemInfo = dataclasses.field(kw_only=True, default=None)
    n: int = dataclasses.field(kw_only=True)


class ItemInfoGroupAssembly(abc.ABCMeta):
    def __new__(cls, name, bases, attrs):
        prefix = "seperate_"
        field_name = "seperate_items"
        seperate_items = attrs[field_name] = {}

        seperate = {name[len(prefix):].lower(): item for name, item in attrs.items() if
                    name.startswith(prefix)
                    and name != field_name
                    and isinstance(item, ParaboxSeperateItemInfo)}
        seperate_items.update(seperate)
        return super(ItemInfoGroupAssembly, cls).__new__(cls, name, bases, attrs)


class ItemInfoGroup:
    # superclass
    # @property items: list[ParaboxItemDefinition]
    # def get_pool_items(options) to get items in pool for options
    # def post_get_pool_items(options, items) hook to modify items
    # item_selection will not be needed anymore
    # some way to get requirement for current options (eg. opt.progressive, sep_box -> prog_2)
    # make special subclass for Requirement (eg. ReqSingleItem(SingleItem, Req))
    # one class contains all Items (getItems(options) and getAllItems)
    # Requirements are manually referenced by the world generators
    # Requirements can be used by the world for levels

    @classmethod
    @abstractmethod
    def get_option(cls, options: ParaboxOptionValues) -> int:
        pass


class SingleItemInfoGroup(ItemInfoGroup, abc.ABC):
    single: ParaboxSingleItemInfo


class ProgressiveItemInfoGroup(ItemInfoGroup, abc.ABC):
    single: ParaboxSingleItemInfo
    progressive: ParaboxProgressiveItemInfo


class SeperateItemInfoGroup(ItemInfoGroup, abc.ABC, metaclass=ItemInfoGroupAssembly):
    single: ParaboxSingleItemInfo
    progressive: ParaboxProgressiveItemInfo
    seperate_items: dict[str, ParaboxSeperateItemInfo]


class ParaboxItemInfoDefinitions:
    priority = ParaboxItemInfo("Priority", 1)
    extrude = ParaboxItemInfo("Extrude", 2)
    inner_push = ParaboxItemInfo("Inner Push", 3)
    block = ParaboxItemInfo("Block", 4)
    level_select = ParaboxItemInfo("Level Select", 5)
    clone = ParaboxItemInfo("Clone", 6)
    open_main_level = ParaboxItemInfo("Open Main Level", 7)
    even = ParaboxItemInfo("Even", 8)
    oblong = ParaboxItemInfo("Oblong", 9)
    one = ParaboxItemInfo("One", 10)

    recursion = ParaboxSingleItemInfo("Recursion", 11)
    progressive_recursion = ParaboxProgressiveItemInfo("Progressive Recursion", 12, single_item=recursion)

    flip = ParaboxSingleItemInfo("Flip", 13)
    progressive_flip = ParaboxProgressiveItemInfo("Progressive Flip", 14, single_item=flip)

    friend = ParaboxSingleItemInfo("Friend", 15)
    progressive_friend = ParaboxProgressiveItemInfo("Progressive Friend", 16, single_item=friend)

    infinite_exit_block = ParaboxSingleItemInfo("Infinite Exit", 17)
    progressive_infinite_exit_block = ParaboxProgressiveItemInfo("Progressive Infinite Exit", 18,
                                                                 single_item=infinite_exit_block)

    infinite_enter_block = ParaboxSingleItemInfo("Infinite Enter", 19)
    progressive_infinite_enter_block = ParaboxProgressiveItemInfo("Progressive Infinite Enter", 20,
                                                                  single_item=infinite_enter_block)

    player = ParaboxSingleItemInfo("Player", 21)
    progressive_player = ParaboxProgressiveItemInfo("Progressive Player", 22, single_item=player)

    undo = ParaboxSingleItemInfo("Undo", 23)
    progressive_undo = ParaboxProgressiveItemInfo("Progressive Undo", 24, single_item=undo)

    possess = ParaboxSingleItemInfo("Possess", 25)
    progressive_possess = ParaboxProgressiveItemInfo("Progressive Possess", 26, single_item=possess)
    possess_wall = ParaboxSeperateItemInfo("Possess Wall", 27, progressive_item=progressive_possess, n=1)
    possess_box = ParaboxSeperateItemInfo("Possess Box", 28, progressive_item=progressive_possess, n=2)

    nested_button = ParaboxSingleItemInfo("Nested Button", 29)
    progressive_nested_button = ParaboxProgressiveItemInfo("Progressive Nested Button", 30, single_item=nested_button)
    nested_box_button = ParaboxSeperateItemInfo("Nested Box Button", 31,
                                                progressive_item=progressive_nested_button, n=1)
    nested_player_button = ParaboxSeperateItemInfo("Nested Player Button", 32,
                                                   progressive_item=progressive_nested_button, n=2)

    slowness_trap = ParaboxItemInfo("Slowness Trap", 40, ParaboxItemType.TRAP)
    zoom_in_trap = ParaboxItemInfo("Zoom In Trap", 41, ParaboxItemType.TRAP)
    zoom_out_trap = ParaboxItemInfo("Zoom Out Trap", 42, ParaboxItemType.TRAP)
    ascii_trap = ParaboxItemInfo("Ascii Trap", 43, ParaboxItemType.TRAP)
    Rainbow_trap = ParaboxItemInfo("Rainbow Trap", 44, ParaboxItemType.TRAP)
    control_trap = ParaboxItemInfo("Control Trap", 45, ParaboxItemType.TRAP)

    info = ParaboxItemInfo("Info", 46, ParaboxItemType.USEFUL)
    puzzle_skip = ParaboxItemInfo("Puzzle Skip", 47, ParaboxItemType.USEFUL)
    puzzle_help = ParaboxItemInfo("Puzzle Help", 48, ParaboxItemType.USEFUL)
    open_puzzle_help = ParaboxItemInfo("Open Puzzle Help", 49, ParaboxItemType.USEFUL)
    center_puzzle_help = ParaboxItemInfo("Center Puzzle Help", 50, ParaboxItemType.USEFUL)
    exit_puzzle_help = ParaboxItemInfo("Exit Puzzle Help", 51, ParaboxItemType.USEFUL)

    # EXPERIMENTAL #
    l_full_box_3 = ParaboxItemInfo("L Full Box (3)", 60)
    t_full_box_3 = ParaboxItemInfo("T Full Box (3)", 61)
    i_full_box_3 = ParaboxItemInfo("I Full Box (3)", 62)

    pi_full_box_3 = ParaboxItemInfo("PI Full Box (3)", 63)
    bi_full_box_3 = ParaboxItemInfo("BI Full Box (3)", 64)
    bi_b_full_box_3 = ParaboxItemInfo("BI B Full Box (3)", 65)

    d_full_box_3 = ParaboxItemInfo(". Full Box (3)", 66)
    bd_full_box_3 = ParaboxItemInfo("B. Full Box (3)", 67)

    empty_box_3 = ParaboxItemInfo("Empty Box (3)", 68)
    b_empty_box_3 = ParaboxItemInfo("B Empty Box (3)", 69)
    p_empty_box_3 = ParaboxItemInfo("P Empty Box (3)", 70)
    w_empty_box_3 = ParaboxItemInfo("W Empty Box (3)", 71)

    l_full_box_5 = ParaboxItemInfo("L Full Box (5)", 72)
    i_full_box_5 = ParaboxItemInfo("I Full Box (5)", 73)

    empty_box_5 = ParaboxItemInfo("Empty Box (5)", 74)
    b_empty_box_5 = ParaboxItemInfo("B Empty Box (5)", 75)
    p_empty_box_5 = ParaboxItemInfo("P Empty Box (5)", 76)
    w_empty_box_5 = ParaboxItemInfo("W Empty Box (5)", 77)

    bj_b_full_box_5 = ParaboxItemInfo("BJ B Full Box (5)", 78)
    bol_full_box_5 = ParaboxItemInfo("BOL Full Box (5)", 79)
    d_hollow_box_5 = ParaboxItemInfo(". Hollow Box (5)", 80)
    dd_hollow_box_5 = ParaboxItemInfo(".. Hollow Box (5)", 81)
    open_hollow_box_5 = ParaboxItemInfo("Open Hollow Box (5)", 82)
    line_empty_box_5 = ParaboxItemInfo("Line Empty Box (5)", 83)
    bbi_full_box_5 = ParaboxItemInfo("BBI Full Box (5)", 84)
    bxi_full_box_5 = ParaboxItemInfo("BXI Full Box (5)", 85)
    # EXPERIMENTAL #


class Possess(SeperateItemInfoGroup):
    @classmethod
    def get_option(cls, options: ParaboxOptionValues) -> int:
        return options.shuffle_possess

    single = ParaboxSingleItemInfo("Possess", 25)
    progressive = ParaboxProgressiveItemInfo("Progressive Possess", 26)
    seperate_wall = ParaboxSeperateItemInfo("Possess Wall", 27, n=1)
    seperate_box = ParaboxSeperateItemInfo("Possess Box", 28, n=2)


@dataclass(frozen=True)
class ParaboxItemGenerator:
    start_id: int

    @property
    @abstractmethod
    def items(self) -> list[ParaboxItemInfo]:
        pass


@dataclass(frozen=True)
class KeyDefinition:
    name: str
    symbol: str
    id: int


@dataclass(frozen=True)
class KeyItemDefinition(KeyDefinition):
    pass


key_definitions = [
    KeyDefinition("Alpha", "α", 1),
    KeyDefinition("Beta", "β", 2),
    KeyDefinition("Gamma", "γ", 3),
    KeyDefinition("Delta", "δ", 4),
    KeyDefinition("Zeta", "ζ", 5),
    KeyDefinition("Eta", "η", 6),
    KeyDefinition("Theta", "θ", 7),
    KeyDefinition("Iota", "ι", 8),
    KeyDefinition("Kappa", "κ", 9),
    KeyDefinition("Lambda", "λ", 10),
    KeyDefinition("Mu", "μ", 11),
    KeyDefinition("Nu", "ν", 12),
    KeyDefinition("Xi", "ξ", 13),
    KeyDefinition("Omikron", "ο", 14),
    KeyDefinition("Pi", "π", 15),
    KeyDefinition("Rho", "ρ", 16),
    KeyDefinition("Sigma", "σ", 17),
    KeyDefinition("Tau", "τ", 18),
    KeyDefinition("Upsilon", "υ", 19),
    KeyDefinition("Phi", "φ", 20),
    KeyDefinition("Chi", "χ", 21),
    KeyDefinition("Psi", "ψ", 23),
    KeyDefinition("Omega", "ω", 24)
]

world_name_definitions = [
    "Intro",
    "Enter",
    "Empty",
    "Eat",
    "Reference",
    "Swap",
    "Center",
    "Clone",
    "Transfer",
    "Open",
    "Flip",
    "Cycle",
    "Player",
    "Possess",
    "Wall",
    "Infinite Exit",
    "Infinite Enter",
    "Multi Infinite",
    "Reception",
    "Challenge",
    "Gallery",
    "Appendix",
    "Appendix: Priority",
    "Appendix: Extrude",
    "Appendix: Inner Push"
]


@dataclass(frozen=True)
class KeyItemGenerator(ParaboxItemGenerator):
    @functools.cached_property
    def items(self) -> list[ParaboxItemInfo]:
        return [ParaboxItemInfo(k.name, k.id) for k in self.definitions]

    @functools.cached_property
    def definitions(self) -> list[KeyItemDefinition]:
        return [KeyItemDefinition(f"{k.name} Key", k.symbol, self.start_id + k.id) for k in key_definitions]


@dataclass(frozen=True)
class LevelSelectItemGenerator(ParaboxItemGenerator):
    @functools.cached_property
    def items(self) -> list[ParaboxItemInfo]:
        return [ParaboxItemInfo(
            f"Level Select ({name})",
            self.start_id + idx,
            ParaboxItemType.USEFUL
        ) for idx, name in enumerate(world_name_definitions)]


class ParaboxItemInfoGeneratorDefinitions:
    keys = KeyItemGenerator(100)
    level_selects = LevelSelectItemGenerator(200)
    # TODO: Box Sizes


def get_item_name_to_id():
    def create_pairs():
        value: ParaboxItemInfo
        for attr, value in ParaboxItemInfoDefinitions.__dict__.items():
            if not attr.startswith("__"):
                yield value.name, value.id
        generator: ParaboxItemGenerator
        for attr, generator in ParaboxItemInfoGeneratorDefinitions.__dict__.items():
            if not attr.startswith("__"):
                yield from [(v.name, v.id) for v in generator.items]

    return dict(create_pairs())


item_name_to_id = get_item_name_to_id()
key_name_to_symbol = {k.name: k.symbol for k in key_definitions}


def main():
    def print_dict(d: dict[Any, Any]):
        print("\n".join([str(v) + " " * (6 - len(str(v))) + k for k, v in d.items()]))

    print_dict(item_name_to_id)
    print("\n" * 3)
    print_dict(key_name_to_symbol)
    print("\n" * 3)
    print_dict(Possess.seperate_items)


if __name__ == '__main__':
    main()
