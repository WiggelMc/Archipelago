from worlds.parabox.external.generator_access import GeneratorAccessor


def generate_item_name_to_id() -> dict[str, int]:
    items = [item for provider in GeneratorAccessor.item_providers for item in provider.items]
    return {i.name: i.id for i in items}


item_name_to_id = generate_item_name_to_id()
