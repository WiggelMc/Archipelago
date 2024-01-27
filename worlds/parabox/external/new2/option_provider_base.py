from abc import abstractmethod
from enum import Enum


class OptionValue(Enum):
    pass


class Option:
    display_name: str
    default: OptionValue
    description: str
    class_name: str
    key_name: str


class OptionProvider:
    @classmethod
    @abstractmethod
    def option(cls, options: dict[str, int]) -> Option:
        pass
