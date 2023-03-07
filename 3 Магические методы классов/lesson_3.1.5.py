class LessonItem:
    """lesson = LessonItem(название урока, число практических занятий, общая длительность урока)
    title - название урока (строка);
    practices - число практических занятий (целое положительное число);
    duration - общая длительность урока (целое положительное число)."""

    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if key == "title" and type(value) == str:
            object.__setattr__(self, key, value)
        elif (key == "practices" or key == "duration") and type(value) == int and value > 0:
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __getattr__(self, item):
        if item not in ("title", "practices", "duration"):
            return False

    def __delattr__(self, item):
        if item not in ("title", "practices", "duration"):
            object.__delattr__(self, item)
        else:
            raise AttributeError(f"Атрибут {item} удалять запрещено.")


class Module:
    """module = Module(название модуля)
    Каждый объект класса Module должен содержать локальные атрибуты:
    name - название модуля;
    lessons - список из уроков (объектов класса LessonItem), входящих в модуль (изначально список пуст)."""

    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        if indx in range(len(self.lessons)):
            self.lessons.pop(indx)


class Course:
    """course = Course(название курса)
    И содержат следующие локальные атрибуты:
    name - название курса (строка);
    modules - список модулей в курсе (изначально список пуст)."""
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        if indx in range(len(self.modules)):
            self.modules.pop(indx)


course = Course("Python ООП")
module_1 = Module("Часть первая")
module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
module_1.add_lesson(LessonItem("Урок 3", 5, 800))
course.add_module(module_1)
module_2 = Module("Часть вторая")
module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
course.add_module(module_2)

print(f"{course.name}")
for _module in course.modules:
    print(f"\t{_module.name}")
    for _lessons in _module.lessons:
        print(f"\t\t{_lessons.title}")
