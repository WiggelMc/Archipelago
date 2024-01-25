from items_base import ItemInfoTrap, ParaboxTrapItemInfo
from option_values import ParaboxOptionValues


class SlownessTrap(ItemInfoTrap):
    @classmethod
    def get_option(cls, options: ParaboxOptionValues) -> int:
        return options.enable_slowness_trap

    item = ParaboxTrapItemInfo("Slowness Trap", 40)


class ZoomInTrap(ItemInfoTrap):
    @classmethod
    def get_option(cls, options: ParaboxOptionValues) -> int:
        return options.enable_zoom_in_trap

    item = ParaboxTrapItemInfo("Zoom In Trap", 41)


class ZoomOutTrap(ItemInfoTrap):
    @classmethod
    def get_option(cls, options: ParaboxOptionValues) -> int:
        return options.enable_zoom_out_trap

    item = ParaboxTrapItemInfo("Zoom Out Trap", 42)


class AsciiTrap(ItemInfoTrap):
    @classmethod
    def get_option(cls, options: ParaboxOptionValues) -> int:
        return options.enable_ascii_trap

    item = ParaboxTrapItemInfo("Ascii Trap", 43)


class RainbowTrap(ItemInfoTrap):
    @classmethod
    def get_option(cls, options: ParaboxOptionValues) -> int:
        return options.enable_rainbow_trap

    item = ParaboxTrapItemInfo("Rainbow Trap", 44)


class ControlTrap(ItemInfoTrap):
    @classmethod
    def get_option(cls, options: ParaboxOptionValues) -> int:
        return options.enable_control_trap

    item = ParaboxTrapItemInfo("Control Trap", 45)


if __name__ == '__main__':
    # noinspection PyTypeChecker
    A1 = type("Fish", (ControlTrap,), {})
    A1: type[ControlTrap]
    print(ControlTrap().item)
