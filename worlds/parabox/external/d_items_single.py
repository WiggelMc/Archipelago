from .items_seperate import SeperateItemDefinition, SeperateOptionValue, SeperateOption
from .items_progressive import ProgressiveOption, ProgressiveOptionValue, ProgressiveItemDefinition
from .items_single import SingleItemDefinition, SingleOptionValue, SingleOption
from .items_base import SingleReqItem, SingleItem, ProgressiveReqItem, ProgressiveItem, SeperateReqItem
from .generate_decorator import generate


def init():
    pass


@generate
class Priority(SingleItemDefinition):
    opt = SingleOption(default=SingleOptionValue.Single, description_text="""
        This does that
    """)
    single = SingleReqItem(id_offset=1)


@generate
class Recursion(ProgressiveItemDefinition):
    opt = ProgressiveOption(default=ProgressiveOptionValue.Progressive, description_text="""
        This is another text
        Yeah
    """)
    single = SingleItem(id_offset=2)
    progressive = ProgressiveReqItem(id_offset=3)
    progressive_amount = 2


@generate
class Possess(SeperateItemDefinition):
    opt = SeperateOption(default=SeperateOptionValue.Seperate, description_text="""
        This time there will be more text. This might be difficult to read, but it exists to test exactly that case.
        More Text could be written, but there will never be another text this long.
        Might need more love.
        Text is cool.
        This option is quite extensive
    """)
    single = SingleItem(id_offset=4)
    progressive = ProgressiveItem(id_offset=5)
    seperate_wall = SeperateReqItem(id_offset=6, name="Possess Wall", stage=1)
    seperate_box = SeperateReqItem(id_offset=7, name="Possess Box", stage=2)


if __name__ == '__main__':
    print(Priority.opt.description)
    print(str(Priority.opt.__dict__).replace(",", "\n\n"))
    print(str(Priority.single.__dict__).replace(",", "\n\n"))
    print(Priority.items)
    print(Recursion.items)
    print(Possess.items)
