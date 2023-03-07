class Property:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'
        self.min = owner.MIN_DIMENSION
        self.max = owner.MAX_DIMENSION

    def __get__(self, instance, owner):
        if instance:
            return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.min <= value <= self.max:
            setattr(instance, self.name, value)


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    a = Property()
    b = Property()
    c = Property()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        object.__setattr__(self, key, value)


def type(arg):
    return property

