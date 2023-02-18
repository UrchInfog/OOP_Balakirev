class Car:
    __model = None

    @property
    def model(self):
        if self.check_attr(self.__model):
            return self.__model

    @model.setter
    def model(self, __model):
        if self.check_attr(__model):
            self.__model = __model

    @classmethod
    def check_attr(self, __model):
        if type(__model) == str and 2 <= len(__model) <= 100:
            return True
        else:
            return False


m = Car()
m.model = "Нива"
print(m.model)
m.model = 123
print(m.model)