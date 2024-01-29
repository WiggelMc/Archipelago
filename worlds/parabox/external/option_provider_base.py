import typing
from abc import abstractmethod
from enum import Enum
from typing import Any


class Option:
    display_name: str
    default: Any
    description: str
    class_name: str
    key_name: str


class OptionProvider:
    @classmethod
    @abstractmethod
    def option(cls, options: dict[str, int]) -> Option:
        pass

    opt: Option


class EnumOptionValue(Enum):
    pass


class EnumOption(Option):
    enum: typing.ClassVar[type[EnumOptionValue]]
    default: EnumOptionValue


class EnumOptionProvider(OptionProvider):
    @classmethod
    @abstractmethod
    def option(cls, options: dict[str, int]) -> EnumOption:
        pass

    opt: EnumOption


class RangeOption(Option):
    default: int
    min: int
    max: int


class RangeOptionProvider(OptionProvider):
    @classmethod
    @abstractmethod
    def option(cls, options: dict[str, int]) -> RangeOption:
        pass

    opt: RangeOption
