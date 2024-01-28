from .option_access import get_item_providers


def generate_item_name_to_id() -> dict[str, int]:
    item_providers = get_item_providers()
    items = [item for provider in item_providers for item in provider.items]
    return {i.name: i.id for i in items}


item_name_to_id = generate_item_name_to_id()
