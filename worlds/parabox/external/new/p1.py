from abc import ABC, ABCMeta, abstractmethod
from typing import Any


class Accessor:
    a_val: str


class Definer:
    a_def: str


class NotDefinedHereError(Exception):
    pass


class Acc:
    def __init__(self, attrs):
        self._attrs = attrs

    _attrs: dict[str, Any]

    def __setattr__(self, key, value):
        if key == "_attrs":
            super().__setattr__(key, value)
        else:
            self._attrs[key] = value


class Def:
    def __init__(self, attrs):
        self._attrs = attrs

    _attrs: dict[str, Any]

    def __getattr__(self, item):
        try:
            return self._attrs[item]
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

        return super().__new__(cls, name, bases, attrs)


class Combiner(Accessor, Definer, metaclass=MetaA):
    pass


class Tester(Combiner):
    a_def = "Test"


class Tester2(Combiner):
    a_def = "Te  st2"

    @abstractmethod
    def f(self):
        pass


class AbcMetaA(MetaA, ABCMeta):
    pass


class Tester3(Tester2, ABC, metaclass=AbcMetaA):
    pass


if __name__ == '__main__':
    print(Tester.a_val)
    print(Tester2.a_val)
    print(Tester3.a_val)
    print(Tester3.a_val)
    print("  ")
