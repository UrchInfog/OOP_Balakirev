class Museum:
    def __init__(self, name):
        self.name = name
        self.exhibits = []

    def add_exhibit(self, obj):
        self.exhibits.append(obj)

    def remove_exhibit(self, obj):
        if obj in self.exhibits:
            self.exhibits.remove(obj)

    def get_info_exhibit(self, indx):
        return f"Описание экспоната {self.exhibits[indx].name}: {self.exhibits[indx].descr}"

    # def __getattribute__(self, item):
    #     if item == "descr":
    #         print(f"Описание экспоната {object.__getattribute__(self, 'name')}: {object.__getattribute__(self, item)}")
    #         return object.__getattribute__(self, item)
    #     else:
    #         return object.__getattribute__(self, item)

class Picture:
    # локальные атрибуты: name - название; author - художник; descr - описание
    def __init__(self, name, author, descr):
        self.name = name
        self.author = author
        self.descr = descr

class Mummies:
    # локальные атрибуты: name - имя мумии; location - место находки; descr - описание
    def __init__(self, name, location, descr):
        self.name = name
        self.location = location
        self.descr = descr

class Papyri:
    # локальные атрибуты: name - название папируса; date - датировка (строка); descr - описание
    def __init__(self, name, date, descr):
        self.name = name
        self.date = date
        self.descr = descr


mus = Museum("Эрмитаж")
print(mus.name)
mus.add_exhibit(Picture("Балакирев с подписчиками пишет письмо иноземному султану", "Неизвестный автор", "Вдохновляющая, устрашающая, волнующая картина"))
mus.add_exhibit(Mummies("Балакирев", "Древняя Россия", "Просветитель XXI века, удостоенный мумификации"))
p = Papyri("Ученья для, не злата ради", "Древняя Россия", "Самое древнее найденное рукописное свидетельство о языках программирования")
mus.add_exhibit(p)
for x in mus.exhibits:
    print(x.descr)

a = mus.get_info_exhibit(0)
print(a)