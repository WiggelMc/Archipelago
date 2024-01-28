from .items_single import SingleItemDefinition, SingleOptionValue, SingleOption
from worlds.parabox.external.new2.items_base import SingleReqItem
from .generate_decorator import generate


def init():
    pass


@generate
class Priority(SingleItemDefinition):
    opt = SingleOption(default=SingleOptionValue.Single, description_text="""
        This does that
    """)
    single = SingleReqItem(id_offset=1)


if __name__ == '__main__':
    print(Priority.opt.description)
    print(str(Priority.opt.__dict__).replace(",", "\n\n"))
    print(str(Priority.single.__dict__).replace(",", "\n\n"))
    print(Priority.items)
