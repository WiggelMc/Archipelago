import typing
from dataclasses import dataclass


@dataclass
class ValueDef:
    name: str


class ValueAcc:
    name_len: int


@dataclass
class Value(ValueDef, ValueAcc):
    pass


class StuffAcc:
    name_len: int
    values: dict[str, Value]


class StuffDef:
    name: str


class Stuff(StuffDef, StuffAcc):
    pass


TStuff = typing.TypeVar("TStuff", bound=Stuff)


def _init_value(value: Value, cls: TStuff):
    value.name_len = len(value.name)


def generate_stuff(cls: TStuff) -> TStuff:
    cls.name_len = len(cls.name)
    k: str
    prefix = "value_"
    values = {k: v for k, v in cls.__dict__.items() if k.startswith(prefix)}
    cls.values = {k[len(prefix):]: v for k, v in values.items()}
    for k, v in values.items():
        _init_value(v, cls)
    return cls


@generate_stuff
class DefinitionA(Stuff):
    name = "Test"
    value_one = Value("One")
    value_two = Value("Twos")


if __name__ == '__main__':
    # print(DefinitionA.accessor.name_len)
    # print(DefinitionA.accessor.values)
    # print(DefinitionA.value_one)
    print(DefinitionA.value_one.name_len)
    print(list(DefinitionA.values.values())[0].name_len)
    print(int)
