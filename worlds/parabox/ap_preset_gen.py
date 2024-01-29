from worlds.parabox.external.generator_access import GeneratorAccessor
from worlds.parabox.external.items_base import StackedItemDefinition


def generate_presets():
    return {
        "No Elements": {
            p.opt.key_name: 1 for p in GeneratorAccessor.enum_option_providers
            if isinstance(p, StackedItemDefinition) and p.opt.default.value > 1
        }
    }


options_presets: dict[str, dict[str, int]] = generate_presets()
