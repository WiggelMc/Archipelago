from enum import Enum
from typing import NamedTuple


class ParaboxItemType(Enum):
    PROGRESSION = 1
    USEFUL = 2
    TRAP = 3


class ParaboxItemInfo(NamedTuple):
    name: str
    id: int
    item_type: ParaboxItemType = ParaboxItemType.PROGRESSION

    def typed(self, item_type: ParaboxItemType):
        return ParaboxItemInfo(self.name, self.id, item_type)


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

    recursion = ParaboxItemInfo("Recursion", 11)
    progressive_recursion = ParaboxItemInfo("Progressive Recursion", 12)
    flip = ParaboxItemInfo("Flip", 13)
    progressive_flip = ParaboxItemInfo("Progressive Flip", 14)
    friend = ParaboxItemInfo("Friend", 15)
    progressive_friend = ParaboxItemInfo("Progressive Friend", 16)
    infinite_exit_block = ParaboxItemInfo("Infinite Exit", 17)
    progressive_infinite_exit_block = ParaboxItemInfo("Progressive Infinite Exit", 18)
    infinite_enter_block = ParaboxItemInfo("Infinite Enter", 19)
    progressive_infinite_enter_block = ParaboxItemInfo("Progressive Infinite Enter", 20)
    player = ParaboxItemInfo("Player", 21)
    progressive_player = ParaboxItemInfo("Progressive Player", 22)
    undo = ParaboxItemInfo("Undo", 23)
    progressive_undo = ParaboxItemInfo("Progressive Undo", 24)

    possess = ParaboxItemInfo("Possess", 25)
    progressive_possess = ParaboxItemInfo("Progressive Possess", 26)
    possess_wall = ParaboxItemInfo("Possess Wall", 27)
    possess_box = ParaboxItemInfo("Possess Box", 28)


def get_item_name_to_id():
    def create_pairs():
        value: ParaboxItemInfo
        for attr, value in ParaboxItemInfoDefinitions.__dict__.items():
            if not attr.startswith("__"):
                yield value.name, value.id

    return dict(create_pairs())


if __name__ == '__main__':
    print(get_item_name_to_id())
