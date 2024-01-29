import dataclasses
import typing
from dataclasses import dataclass

from Options import PerGameCommonOptions, Choice
from worlds.parabox.external.option_access import get_enum_option_providers

option_providers = get_enum_option_providers()


def get_option_dict():
    options = {}
    for provider in option_providers:
        opt = provider.opt
        opt_enum = type(opt.default)
        opt_dict = {f"option_{v.name}": v.value for v in opt_enum}
        opt_dict.update({
            "default": opt.default.value,
            "display_name": opt.display_name,
            "__doc__": opt.description.replace("\n", "\n    ")
        })
        options[opt.key_name] = type(opt.class_name, (Choice,), opt_dict)
    return options


TOptions = typing.TypeVar("TOptions", bound=PerGameCommonOptions)


def generate_options() -> type[TOptions]:
    options = type("ParaboxOptions", (PerGameCommonOptions,), {
        "__annotations__": get_option_dict()
    })
    assert issubclass(options, PerGameCommonOptions)
    options = dataclass(options)
    return options


ParaboxOptions: type[TOptions] = generate_options()


def options_to_dict(options: ParaboxOptions) -> dict[str, int]:
    return options.as_dict(*[field.name for field in dataclasses.fields(ParaboxOptions)], casing="snake")
