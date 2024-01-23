def inherit_docstring(cls: type):
    if not cls.__doc__:
        for parent in cls.__mro__[1:-1]:
            if parent.__doc__:
                cls.__doc__ = parent.__doc__
                break
    return cls
