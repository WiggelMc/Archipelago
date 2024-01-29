from generate_values import get_option_providers

if __name__ == '__main__':
    print([o.option_definition for o in get_option_providers()])
