from .generator import generate
from .items_base import SingleItem, ProgressiveReqItem
from .items_progressive import ProgressiveItemDefinition, ProgressiveOption, \
    ProgressiveOptionValue


def init():
    pass


@generate
class Recursion(ProgressiveItemDefinition):
    opt = ProgressiveOption(default=ProgressiveOptionValue.Progressive, description_text="""
        TODO: Option Description
    """)
    single = SingleItem(id_offset=15)
    progressive = ProgressiveReqItem(id_offset=16)
    progressive_amount = 2


@generate
class Flip(ProgressiveItemDefinition):
    opt = ProgressiveOption(default=ProgressiveOptionValue.Progressive, description_text="""
        TODO: Option Description
    """)
    single = SingleItem(id_offset=17)
    progressive = ProgressiveReqItem(id_offset=18)
    progressive_amount = 2


@generate
class Friend(ProgressiveItemDefinition):
    opt = ProgressiveOption(default=ProgressiveOptionValue.Progressive, description_text="""
        TODO: Option Description
    """)
    single = SingleItem(id_offset=19)
    progressive = ProgressiveReqItem(id_offset=20)
    progressive_amount = 4


@generate
class InfiniteExitBlock(ProgressiveItemDefinition):
    opt = ProgressiveOption(default=ProgressiveOptionValue.Progressive, description_text="""
        TODO: Option Description
    """)
    single = SingleItem(id_offset=21)
    progressive = ProgressiveReqItem(id_offset=22)
    progressive_amount = 4


@generate
class InfiniteEnterBlock(ProgressiveItemDefinition):
    opt = ProgressiveOption(default=ProgressiveOptionValue.Progressive, description_text="""
        TODO: Option Description
    """)
    single = SingleItem(id_offset=23)
    progressive = ProgressiveReqItem(id_offset=24)
    progressive_amount = 4


@generate
class Player(ProgressiveItemDefinition):
    opt = ProgressiveOption(default=ProgressiveOptionValue.Progressive, description_text="""
        TODO: Option Description
    """)
    single = SingleItem(id_offset=25)
    progressive = ProgressiveReqItem(id_offset=26)
    progressive_amount = 2


@generate
class Undo(ProgressiveItemDefinition):
    opt = ProgressiveOption(default=ProgressiveOptionValue.Unlocked, description_text="""
        TODO: Option Description
    """)
    single = SingleItem(id_offset=27)
    progressive = ProgressiveReqItem(id_offset=28)
    progressive_amount = 2
