class Clock:
    def __init__(self, time=0):
        self.__time = time

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def __check_time(self, tm):
        if type(tm) == int and 0 <= tm < 100_000:
            return True
        else:
            return False

    def get_time(self):
        return self.__time

clock = Clock(4530)