from __future__ import annotations

import dataclasses
from dataclasses import dataclass
from enum import Enum
from typing import Any

import shuffle_items, world_items, key_items
from key_items import key_name_to_symbol
from items_base import ParaboxItemGenerator


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


class ParaboxItemInfoDefinitions:
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


class ParaboxItemInfoGeneratorDefinitions:
    priority = shuffle_items.Priority()
    extrude = shuffle_items.Extrude()
    inner_push = shuffle_items.InnerPush()
    block = shuffle_items.Block()
    level_select = shuffle_items.LevelSelect()
    clone = shuffle_items.Clone()
    open_main_level = shuffle_items.Open()
    even = shuffle_items.Even()
    oblong = shuffle_items.Oblong()
    one = shuffle_items.One()

    recursion = shuffle_items.Recursion()
    flip = shuffle_items.Flip()
    friend = shuffle_items.Friend()
    infinite_exit_block = shuffle_items.InfiniteExitBlock()
    infinite_enter_block = shuffle_items.InfiniteEnterBlock()
    player = shuffle_items.Player()
    undo = shuffle_items.Undo()

    possess = shuffle_items.Possess()
    nested_button = shuffle_items.NestedButton()

    keys = key_items.KeyItemGenerator(100)
    level_selects = world_items.LevelSelectItemGenerator(200)


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


def main():
    def print_dict(d: dict[Any, Any]):
        print("\n".join([str(v) + " " * (6 - len(str(v))) + k for k, v in d.items()]))

    print_dict(item_name_to_id)
    print("\n" * 3)
    print_dict(key_name_to_symbol)
    print("\n" * 3)
    print(shuffle_items.Possess().items)


if __name__ == '__main__':
    main()
