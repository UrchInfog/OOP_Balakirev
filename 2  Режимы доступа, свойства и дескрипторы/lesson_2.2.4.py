class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        if self.check_value(x):
            self.__x = x
        else:
            self.__x = 0
        if self.check_value(y):
            self.__y = y
        else:
            self.__y = 0

    @classmethod
    def check_value(cls, value):
        return type(value) in (int, float) and cls.MIN_COORD <= value <= cls.MAX_COORD

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if self.check_value(value):
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if self.check_value(value):
            self.__y = value

    @staticmethod
    def norm2(vector):
        return vector.__x ** 2 + vector.__y ** 2


v1 = RadiusVector2D()        # радиус-вектор с координатами (0; 0)
v2 = RadiusVector2D(1)       # радиус-вектор с координатами (1; 0)
v3 = RadiusVector2D(-1111, -2000)    # радиус-вектор с координатами (1; 2)
print(v3.__dict__)
v3.y = 110123
print(v3.__dict__)