# Получился говнокод

class Circle:
    def __init__(self, x, y, radius):
        self.__x = x
        self.__y = y
        self.__radius = radius

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__x = value

    def __setattr__(self, key, value):
        if key in ("_Circle__x", "_Circle__y", "_Circle__radius") and type(value) not in (int, float):
            raise TypeError("Неверный тип присваиваемых данных.")
        if (key in ("_Circle__radius", "radius") and value > 0) or key in ("_Circle__x", "x", "_Circle__y", "y"):
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

circle = Circle(10.5, 7, 22)
circle.x = 10
circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
x, y = circle.x, circle.y
print(circle.x, circle.y, circle.radius)
res = circle.name # False, т.к. атрибут name не существует
print(res)

assert type(Circle.x) == property and type(Circle.y) == property and type(
    Circle.radius) == property, "в классе Circle должны быть объявлены объекты-свойства x, y и radius"

try:
    cr = Circle(20, '7', 22)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при инициализации объекта с недопустимыми аргументами"

cr = Circle(20, 7, 22)
assert cr.x == 20 and cr.y == 7 and cr.radius == 22, "объекты-свойства x, y и radius вернули неверные значения"

cr.radius = -10  # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
assert cr.radius == 22, "при присваивании некорректного значения, прежнее значение изменилось"

x, y = cr.x, cr.y
assert x == 20 and y == 7, "объекты-свойства x, y вернули некорректные значения"
assert cr.name == False, "при обращении к несуществующему атрибуту должно возвращаться значение False"

try:
    cr.x = '20'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"

cr.y = 7.8
cr.radius = 10.6