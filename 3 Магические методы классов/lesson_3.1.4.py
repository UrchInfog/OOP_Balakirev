class Shop:
    """Класс для управления магазином в целом
    shop = Shop(название магазина)"""

    def __init__(self, name_shop):
        self.name_shop = name_shop
        self.goods = []

    def add_product(self, product):
        """добавление нового товара в магазин (в конец списка goods)"""
        self.goods.append(product)

    def remove_product(self, product):
        """удаление товара product из магазина (из списка goods)"""
        if product in self.goods:
            self.goods.remove(product)


class Product:
    id = 0
    """Класс для представления отдельного товара
    p = Product(название, вес, цена)"""

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        self.set_id(self)

    @classmethod
    def set_id(cls, self):
        cls.id += 1
        self.id = cls.id

    def __setattr__(self, key, value):
        if key == "name" and type(value) == str:
            object.__setattr__(self, key, value)
        elif key in ("weight", "price") and type(value) in (int, float) and value > 0:
            object.__setattr__(self, key, value)
        elif key == "id" and type(value) == int:
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item == "id":
            raise AttributeError("Атрибут id удалять запрещено.")


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
shop.add_product(Product("Python1", 1501, 5121))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}, [{p.id}]")
    del p.id
