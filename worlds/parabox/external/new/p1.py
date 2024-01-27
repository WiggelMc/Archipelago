from dataclasses import dataclass
from typing import Any


class Accessor:
    a_val: str


class Definer:
    a_def: str


class NotDefinedHereError(Exception):
    pass


@dataclass
class Acc:
    attrs: dict[str, Any]

    def __setattr__(self, key, value):
        if key == "attrs":
            super().__setattr__(key, value)
        else:
            self.attrs[key] = value


@dataclass
class Def:
    attrs: dict[str, Any]

    def __getattr__(self, item):
        try:
            return self.attrs[item]
        except KeyError as e:
            raise NotDefinedHereError() from e


class MetaA(type):
    def __new__(cls, name, bases, attrs):
        # noinspection PyTypeChecker
        accessor: Accessor = Acc(attrs)
        # noinspection PyTypeChecker
        definer: Definer = Def(attrs)

        try:
            accessor.a_val = definer.a_def.lower()
            print("NAME: " + name)
        except NotDefinedHereError:
            pass

        return super(MetaA, cls).__new__(cls, name, bases, attrs)


class Combiner(Accessor, Definer, metaclass=MetaA):
    pass


class Tester(Combiner):
    a_def = "Test"


class Tester2(Combiner):
    a_def = "Te  st2"


class Tester3(Tester2):
    pass


# class B(A):
#     a = "A"


# class B(metaclass=MetaA):
#     a = 'B'


if __name__ == '__main__':
    print(Tester.a_val)
    print(Tester2.a_val)
    print(Tester3.a_val)
    print(Tester3.a_val)
