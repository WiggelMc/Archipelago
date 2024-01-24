import functools
from dataclasses import dataclass

from items_base import ParaboxItemGenerator, ParaboxItemInfo, ParaboxItemType

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
class LevelSelectItemGenerator(ParaboxItemGenerator):
    start_id: int

    @functools.cached_property
    def items(self) -> list[ParaboxItemInfo]:
        return [ParaboxItemInfo(
            f"Level Select ({name})",
            self.start_id + idx,
            ParaboxItemType.USEFUL
        ) for idx, name in enumerate(world_name_definitions)]
