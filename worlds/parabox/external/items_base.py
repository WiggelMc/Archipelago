import dataclasses
from abc import abstractmethod, ABC, ABCMeta
from dataclasses import dataclass
from enum import Enum

from option_values import ParaboxOptionValues


class ParaboxItemType(Enum):
    PROGRESSION = 1
    USEFUL = 2
    TRAP = 3


class ParaboxItemGroup(Enum):
    pass


@dataclass(frozen=True)
class ParaboxItemInfo:
    name: str
    id: int
    item_type: ParaboxItemType = ParaboxItemType.PROGRESSION

    def typed(self, item_type: ParaboxItemType):
        return dataclasses.replace(self, item_type=item_type)

@dataclass(frozen=True)
class ParaboxTrapItemInfo(ParaboxItemInfo):
    item_type: ParaboxItemType = ParaboxItemType.TRAP
    pass


@dataclass(frozen=True)
class ParaboxSingleItemInfo(ParaboxItemInfo):
    pass


@dataclass(frozen=True)
class ParaboxProgressiveItemInfo(ParaboxItemInfo):
    pass


@dataclass(frozen=True)
class ParaboxSeperateItemInfo(ParaboxItemInfo):
    n: int = dataclasses.field(kw_only=True)


class ItemInfoGroupAssembly(ABCMeta):
    def __new__(cls, name, bases, attrs):
        prefix = "seperate_"
        field_name = "seperate_items"
        seperate_items = attrs[field_name] = {}

        seperate = {name[len(prefix):].lower(): item for name, item in attrs.items() if
                    name.startswith(prefix)
                    and name != field_name
                    and isinstance(item, ParaboxSeperateItemInfo)}
        seperate_items.update(seperate)
        return super(ItemInfoGroupAssembly, cls).__new__(cls, name, bases, attrs)


@dataclass(frozen=True)
class ParaboxItemGenerator:
    @property
    @abstractmethod
    def items(self) -> list[ParaboxItemInfo]:
        pass

@dataclass(frozen=True)
class ItemInfoDefinition(ParaboxItemGenerator):
    @classmethod
    @abstractmethod
    def get_all_items(cls) -> list[ParaboxItemInfo]:
        pass

    @property
    def items(self) -> list[ParaboxItemInfo]:
        return self.get_all_items()

class OptionDependent:
    @classmethod
    @abstractmethod
    def get_option(cls, options: ParaboxOptionValues) -> int:
        pass


@dataclass(frozen=True)
class ItemInfoTrap(ItemInfoDefinition, OptionDependent, ABC):
    @classmethod
    def get_all_items(cls) -> list[ParaboxItemInfo]:
        return [cls.item]

    item: ParaboxTrapItemInfo


@dataclass(frozen=True)
class ItemInfoGroup(ItemInfoDefinition, OptionDependent, ABC):
    # superclass
    # @property items: list[ParaboxItemDefinition]
    # def get_pool_items(options) to get items in pool for options
    # def post_get_pool_items(options, items) hook to modify items
    # item_selection will not be needed anymore
    # some way to get requirement for current options (eg. opt.progressive, sep_box -> prog_2)
    # make special subclass for Requirement (eg. ReqSingleItem(SingleItem, Req))
    # one class contains all Items (getItems(options) and getAllItems)
    # Requirements are manually referenced by the world generators
    # Requirements can be used by the world for levels
    pass


class SingleItemInfoGroup(ItemInfoGroup, ABC):
    @classmethod
    def get_all_items(cls) -> list[ParaboxItemInfo]:
        return [cls.single]

    single: ParaboxSingleItemInfo


class ProgressiveItemInfoGroup(ItemInfoGroup, ABC):
    @classmethod
    def get_all_items(cls) -> list[ParaboxItemInfo]:
        return [cls.single, cls.progressive]

    single: ParaboxSingleItemInfo
    progressive: ParaboxProgressiveItemInfo


class SeperateItemInfoGroup(ItemInfoGroup, ABC, metaclass=ItemInfoGroupAssembly):
    @classmethod
    def get_all_items(cls) -> list[ParaboxItemInfo]:
        return [cls.single, cls.progressive] + list(cls.seperate_items.values())

    single: ParaboxSingleItemInfo
    progressive: ParaboxProgressiveItemInfo
    seperate_items: dict[str, ParaboxSeperateItemInfo]


if __name__ == '__main__':
    print("EE")
