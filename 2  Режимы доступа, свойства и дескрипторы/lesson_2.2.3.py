class StackObj:
    """Класс для описания объектов односвязного списка"""

    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if type(obj) == StackObj or obj == None:
            self.__next = obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class Stack:
    """Класс для управления односвязным списком"""
    top = None

    def push(self, obj):
        """Добавление объекта класса StackObj в конец односвязного списка"""
        if self.top == None:
            self.top = obj
            obj.next = None
        else:
            last_obj = self.top
            while last_obj.next != None:
                last_obj = last_obj.next
            last_obj.next = obj
            obj.next = None

    def pop(self):
        """извлечение последнего объекта с его удалением из односвязного списка"""
        if self.top:
            if self.top.next == None:
                obj = self.top
                self.top = None
                return obj
            else:
                obj = self.top
                while True:
                    obj_prev = obj
                    obj = obj.next
                    if obj.next == None:
                        obj_prev.next = None
                        return obj_prev
        else:
            return None


    def get_data(self):
        """получение списка из объектов односвязного списка"""
        lst = []
        if self.top:
            obj = self.top
            while obj.next:
                lst.append(obj.data)
                obj = obj.next
            else:
                lst.append(obj.data)
        return lst


s = Stack()
top = StackObj("obj_1")
s.push(top)
s.push(StackObj("obj_2"))
s.push(StackObj("obj_3"))
s.pop()

res = s.get_data()
print(res)

assert res == ["obj_1", "obj_2"], f"метод get_data вернул неверные данные: {res}"
assert s.top == top, "атрибут top объекта класса Stack содержит неверное значение"

h = s.top
while h:
    res = h.data
    h = h.next

s = Stack()
top = StackObj("obj_1")
s.push(top)
s.pop()
assert s.get_data() == [], f"метод get_data вернул неверные данные: {s.get_data()}"

n = 0
h = s.top
while h:
    h = h.next
    n += 1

assert n == 0, "при удалении всех объектов, стек-подобная стурктура оказалась не пустой"

s = Stack()
top = StackObj("name_1")
s.push(top)
obj = s.pop()
assert obj == top, "метод pop() должен возвращать удаляемый объект"


s = Stack()
top = StackObj("obj_1")
s.push(top)
obj = s.pop()
assert isinstance(obj, StackObj), "метод pop() не возвращает объект StackObj"
assert s.get_data() == [], f"метод get_data вернул неверные данные: {s.get_data()}"