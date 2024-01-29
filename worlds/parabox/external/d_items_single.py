from .items_single import SingleItemDefinition, SingleOptionValue, SingleOption
from .items_base import SingleReqItem
from .generator import generate


def init():
    pass


@generate
class Priority(SingleItemDefinition):
    opt = SingleOption(default=SingleOptionValue.Single, description_text="""
        TODO: Option Description
    """)
    single = SingleReqItem(id_offset=1)


@generate
class Extrude(SingleItemDefinition):
    opt = SingleOption(default=SingleOptionValue.Single, description_text="""
        TODO: Option Description
    """)
    single = SingleReqItem(id_offset=2)


@generate
class InnerPush(SingleItemDefinition):
    opt = SingleOption(default=SingleOptionValue.Single, description_text="""
        TODO: Option Description
    """)
    single = SingleReqItem(id_offset=3)


@generate
class Block(SingleItemDefinition):
    opt = SingleOption(default=SingleOptionValue.Single, description_text="""
        TODO: Option Description
    """)
    single = SingleReqItem(id_offset=4)


@generate
class LevelSelect(SingleItemDefinition):
    opt = SingleOption(default=SingleOptionValue.Disabled, description_text="""
        TODO: Option Description
    """)
    single = SingleReqItem(id_offset=5)


@generate
class Clone(SingleItemDefinition):
    opt = SingleOption(default=SingleOptionValue.Single, description_text="""
        TODO: Option Description
    """)
    single = SingleReqItem(id_offset=6)


@generate
class Open(SingleItemDefinition):
    opt = SingleOption(default=SingleOptionValue.Single, description_text="""
        TODO: Option Description
    """)
    single = SingleReqItem(id_offset=7)


@generate
class Even(SingleItemDefinition):
    opt = SingleOption(default=SingleOptionValue.Single, description_text="""
        TODO: Option Description
    """)
    single = SingleReqItem(id_offset=8)


@generate
class Oblong(SingleItemDefinition):
    opt = SingleOption(default=SingleOptionValue.Single, description_text="""
        TODO: Option Description
    """)
    single = SingleReqItem(id_offset=9)


@generate
class One(SingleItemDefinition):
    opt = SingleOption(default=SingleOptionValue.Single, description_text="""
        TODO: Option Description
    """)
    single = SingleReqItem(id_offset=10)
