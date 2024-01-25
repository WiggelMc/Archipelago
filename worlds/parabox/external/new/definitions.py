from __future__ import annotations
from abc import abstractmethod, ABC
from dataclasses import dataclass
from enum import Enum
from typing import Any, Generic, TypeVar


class Option(Enum):
    pass


@dataclass(frozen=True)
class OptionDefinition:
    display_name: str
    default: Option
    description: str


class OptionProvider:
    option_definition: OptionDefinition
    key: str

    @classmethod
    @abstractmethod
    def option(cls, options: dict[str, int]) -> Option:
        pass


class ShuffleSingleOption(Option):
    Disabled = 0
    Unlocked = 1
    Single = 2


class SingleItemDefinition(OptionProvider, ABC):
    @classmethod
    def option(cls, options: dict[str, int]) -> ShuffleSingleOption:
        return ShuffleSingleOption(options[cls.key])


class Priority(SingleItemDefinition):
    key = "shuffle_priority"
    option_definition = OptionDefinition("Shuffle Priority", ShuffleSingleOption.Single, """
        This Options does that
        Bla
        Bla
        Bla
    """)


def remove_whitespace(text: str):
    return "\n".join([line.strip() for line in text.split("\n")])


def main():
    opt = {
        "shuffle_priority": 2
    }
    print(Priority.option(opt))
    print(remove_whitespace(Priority.option_definition.description))


if __name__ == '__main__':
    main()
