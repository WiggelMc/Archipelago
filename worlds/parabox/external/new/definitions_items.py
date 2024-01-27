from generate_decorators import generate
from definitions_base import SingleItemDefinition, ShuffleSingleOption, SingleItemDef, \
    remove_whitespace, OptionDefinition


def init():
    pass


@generate
class Priority(SingleItemDefinition):
    key = "priority"
    option_definition = OptionDefinition(default=ShuffleSingleOption.Single, description="""
        This Options does that
        Bla
        Bla
        Bla
    """)
    single = SingleItemDef("Priority", 1)


def main():
    opt = {
        "shuffle_priority": 2
    }
    print(Priority.option_definition)
    print(Priority.option(opt))
    print(remove_whitespace(Priority.option_definition.description))


if __name__ == '__main__':
    main()
