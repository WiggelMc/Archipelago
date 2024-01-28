from .option_access import get_item_providers


def print_items():
    item_providers = get_item_providers()
    items = [item for provider in item_providers for item in provider.items]
    print("\n".join((str(item) for item in items)))


if __name__ == '__main__':
    print_items()
