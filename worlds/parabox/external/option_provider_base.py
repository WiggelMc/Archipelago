from __future__ import annotations
import typing
from abc import abstractmethod
from enum import Enum
from typing import Any

from .generator import Generator


class Option:
    display_name: str
    default: Any
    description: str
    class_name: str
    key_name: str


option_providers: list[OptionProvider] = []


class OptionProvider(Generator):
    @classmethod
    def _generate(cls):
        option_providers.append(cls())
        super()._generate()

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


enum_option_providers: list[OptionProvider] = []


class EnumOptionProvider(OptionProvider):
    @classmethod
    def _generate(cls):
        enum_option_providers.append(cls())
        super()._generate()

    @classmethod
    @abstractmethod
    def option(cls, options: dict[str, int]) -> EnumOption:
        pass

    opt: EnumOption


class RangeOption(Option):
    default: int
    min: int
    max: int


range_option_providers: list[RangeOptionProvider] = []


class RangeOptionProvider(OptionProvider):
    @classmethod
    def _generate(cls):
        range_option_providers.append(cls())
        super()._generate()

    @classmethod
    @abstractmethod
    def option(cls, options: dict[str, int]) -> RangeOption:
        pass

    opt: RangeOption
