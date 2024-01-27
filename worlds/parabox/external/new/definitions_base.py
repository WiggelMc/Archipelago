from __future__ import annotations
from abc import abstractmethod, ABC
from dataclasses import dataclass
from enum import Enum
from typing import Any, Generic, TypeVar


class Option(Enum):
    pass


@dataclass(frozen=True)
class OptionDefinition:
    display_name: str | None = None
    default: Option | None = None
    description: str | None = None


@dataclass(frozen=True)
class ResolvedOption:
    display_name: str
    default: Option
    description: str


class OptionProvider:
    option_definition: OptionDefinition
    resolved_option: ResolvedOption
    key: str

    @classmethod
    @abstractmethod
    def option(cls, options: dict[str, int]) -> Option:
        pass


class ShuffleSingleOption(Option):
    Disabled = 0
    Unlocked = 1
    Single = 2


@dataclass(frozen=True)
class SingleItemDef:
    name: str
    id: int


class SingleItemDefinition(OptionProvider, ABC):
    @classmethod
    def option(cls, options: dict[str, int]) -> ShuffleSingleOption:
        return ShuffleSingleOption(options["shuffle_" + cls.key])

    single: SingleItemDef


def remove_whitespace(text: str):
    return "\n".join([line.strip() for line in text.split("\n")])
