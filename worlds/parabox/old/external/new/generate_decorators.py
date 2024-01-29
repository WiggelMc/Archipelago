from __future__ import annotations
from definitions_base import OptionProvider

option_providers: list[type[OptionProvider]] = []


def generate(cls: type):
    if issubclass(cls, OptionProvider):
        option_providers.append(cls)
    return cls


if __name__ == '__main__':
    print(option_providers)
