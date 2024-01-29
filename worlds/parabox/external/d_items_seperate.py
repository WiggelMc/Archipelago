from .generator import generate
from .items_base import SingleItem, ProgressiveItem, SeperateReqItem
from .items_seperate import SeperateItemDefinition, SeperateOption, SeperateOptionValue


def init():
    pass


@generate
class Possess(SeperateItemDefinition):
    opt = SeperateOption(default=SeperateOptionValue.Seperate, description_text="""
        TODO: Option Description
    """)
    single = SingleItem(id_offset=40)
    progressive = ProgressiveItem(id_offset=41)
    seperate_wall = SeperateReqItem(id_offset=42, name="Possess Wall", stage=1)
    seperate_box = SeperateReqItem(id_offset=43, name="Possess Box", stage=2)


@generate
class NestedButton(SeperateItemDefinition):
    opt = SeperateOption(default=SeperateOptionValue.Unlocked, description_text="""
        TODO: Option Description
    """)
    single = SingleItem(id_offset=44)
    progressive = ProgressiveItem(id_offset=45)
    seperate_box = SeperateReqItem(id_offset=46, name="Nested Box Button", stage=1)
    seperate_player = SeperateReqItem(id_offset=47, name="Nested Player Button", stage=2)
