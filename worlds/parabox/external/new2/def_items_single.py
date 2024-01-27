from items_single import SingleItemDefinition, SingleOptionValue, SingleOption
from generate_decorator import generate


@generate
class Priority(SingleItemDefinition):
    opt = SingleOption(SingleOptionValue.Single, """
        This does that
    """)
    single = None


if __name__ == '__main__':
    print(Priority.opt.description)
    print(str(Priority.opt.__dict__).replace(",", "\n\n"))
