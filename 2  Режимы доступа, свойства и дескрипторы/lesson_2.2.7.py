class PhoneNumber:
    def __init__(self, number, fio):
        if self.check_number(number):
            self.number = number
        else:
            self.number = None
        self.fio = fio

    def check_number(self, number):
        if type(number) == int and len(str(number)) == 11:
            return True
        else:
            return False

class PhoneBook:
    def __init__(self, obj=None):
        self.phone_book = []
        if obj != None:
            self.phone_book.append(obj)

    def add_phone(self, phone):
        """добавление нового номера телефона (в список)"""
        self.phone_book.append(phone)

    def remove_phone(self, indx):
        """удаление номера телефона по индексу списка"""
        if indx in range(len(self.phone_book)):
            self.phone_book.pop(indx)

    def get_phone_list(self):
        """получение списка из объектов всех телефонных номеров"""
        return self.phone_book

a = PhoneNumber(12345678901, "qwerqwrq")
p = PhoneBook(a)
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
p.remove_phone(1)
print(phones)