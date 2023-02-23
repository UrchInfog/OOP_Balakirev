class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if self.check_num(width):
            self.__width = width
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if self.check_num((height)):
            self.__height = height
            self.show()

    def check_num(self, num):
        return 0 <= num <= 10_000

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")


wnd = WindowDlg("Окошечко", 120, 40)
wnd.width = -123
wnd.height = 13
