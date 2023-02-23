class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.tail:
            self.tail.set_next(obj)
        obj.set_prev(self.tail)
        self.tail = obj
        if not self.head:
            self.head = obj

    def remove_obj(self):
        if self.tail is None:
            return
        prev = self.tail.get_prev()
        if prev:
            prev.set_next(None)
        self.tail = prev
        if self.tail is None:
            self.head = None

    def get_data(self):
        obj = self.head
        tmp = []
        while obj != None:
            tmp.append(obj.get_data())
            obj = obj.get_next()
        return tmp


class ObjList:
    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj):
        """изменение приватного свойства __next на значение obj"""
        self.__next = obj

    def set_prev(self, obj):
        """изменение приватного свойства __prev на значение obj"""
        self.__prev = obj

    def get_next(self):
        """получение значения приватного свойства __next"""
        return self.__next

    def get_prev(self):
        """получение значения приватного свойства __prev"""
        return self.__prev

    def set_data(self, data):
        """изменение приватного свойства __data на значение data"""
        self.__data = data

    def get_data(self):
        """получение значения приватного свойства __data"""
        return self.__data


l = ("Люблю отчизну я, но странною любовью!", "Не победит ее рассудок мой.", "Ни слава, купленная кровью,")

lst = LinkedList()
lst.add_obj(ObjList(l[0]))
lst.add_obj(ObjList(l[1]))
lst.add_obj(ObjList(l[2]))
res = lst.get_data()  # ['данные 1', 'данные 2', 'данные 3']
print(res)
lst.remove_obj()
res = lst.get_data()
print(res)
