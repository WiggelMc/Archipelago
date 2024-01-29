import typing


class Generator:
    @classmethod
    def _generate(cls):
        pass


TAny = typing.TypeVar("TAny", bound=object)


def generate(cls: type[TAny]) -> type[TAny]:
    if not issubclass(cls, Generator):
        return cls

    cls._generate()

    def error_method(c: type[TAny]):
        raise ValueError(f"Tried to apply @generate multiple times on type '{c.__name__}'"
                         f" because it inherits from '{cls.__name__}'")

    cls._generate = classmethod(error_method)
    return cls
