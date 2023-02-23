class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PathLines:
    def __init__(self, *args):
        self.lst_obj = []
        self.lst_obj.extend(args)

    def get_path(self):
        return self.lst_obj

    def add_line(self, line):
        self.lst_obj.append(line)

    def get_length(self):
        if not len(self.lst_obj):
            return 0
        x_start = y_start = 0
        length = []
        for obj in self.lst_obj:
            x, y = obj.x, obj.y
            length.append(((x-x_start)**2 + (y-y_start)**2)**0.5)
            x_start, y_start = x, y
        return sum(length)



p = PathLines(LineTo(1, 2))
print(p.get_length())  # 2.23606797749979
p.add_line(LineTo(10, 20))
p.add_line(LineTo(5, 17))
print(p.get_length())  # 28.191631669843197
m = p.get_path()
print(all(isinstance(i, LineTo) for i in m) and len(m) == 3)  # True

h = PathLines(LineTo(4, 8), LineTo(-10, 30), LineTo(14, 2))
print(h.get_length())  # 71.8992593599813
print(h.get_path())

k = PathLines()
print(k.get_length())  # 0
print(k.get_path())  # []