# Дескрипторы
class Desc:
    def __set_name__(self, owner, name):
        self.instance_name = '_' + owner.__name__ + '__' + name

    def __get__(self, instance, owner):
        if instance:
            return instance.__dict__[self.instance_name]
        else:
            return property()

    def __set__(self, instance, val):
        if type(val) in (int, float) and instance.MIN_DIMENSION <= val <= instance.MAX_DIMENSION:
            instance.__dict__[self.instance_name] = val


# MAIN
class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    a = Desc()
    b = Desc()
    c = Desc()

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def __setattr__(self, key, val):
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        else:
            super().__setattr__(key, val)