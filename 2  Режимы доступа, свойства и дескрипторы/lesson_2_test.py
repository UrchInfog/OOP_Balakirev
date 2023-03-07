class Limits:
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val

    def check_num(self, num):
        return isinstance(num, int) and self.min_val <= num <= self.max_val


class IsInteger:
    # def __init__(self, min_value=0, max_value=1920):
    #     self.min_value = min_value
    #     self.max_value = max_value
    def __init__(self, limit):
        self.limit = limit

    def __set_name__(self, owner, name):
        # self.name = "_" + name
        self.name = name

    def __get__(self, instance, owner):
        # return getattr(instance, self.name)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        # if isinstance(value, int) and self.min_value <= value <= self.max_value:
        if self.limit.check_num(value):
            # setattr(instance, self.name, value)
            instance.__dict__[self.name] = value
        else:
            instance.__dict__[self.name] = None
            # setattr(instance, self.name, None)


class Point2d:
    """Тестовый класс"""
    # x = IsInteger(min_value=0, max_value=1920)
    # y = IsInteger(min_value=0, max_value=1080)
    x = IsInteger(limit=Limits(0, 1920))
    y = IsInteger(limit=Limits(0, 1080))

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(f"self.x = {self.x}, self.y = {self.y}")


ptr = Point2d(10, 200)
print(ptr.__dict__)
ptr.x = 1231
print(ptr.__dict__)
