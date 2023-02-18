class Book:
    def __init__(self, author, title, price):
        self.__author = author
        self.__title = title
        self.__price = price

    def set_author(self, author):
        self.__author = author

    def set_title(self, title):
        self.__title = title

    def set_price(self, price):
        self.__price = price

    def get_author(self):
        return self.__author

    def get_title(self):
        return self.__title

    def get_price(self):
        return self.__price


book = Book("Пушкин А. С.", "Евгений Онегин", 1000)

print(book.get_author(), book.get_title(), book.get_price())
book.set_author("Александр Сергеевич Пушкин")
print(book.get_author(), book.get_title(), book.get_price())
