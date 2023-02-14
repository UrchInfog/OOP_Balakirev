import random
import time


def define_speed(func):
    def wrapper(lst):
        time_start = time.time()
        func(lst)
        time_end = time.time()
        print(f"{func}: время её работы {time_end - time_start} секунд")
    return wrapper


def uniq_1(lst):
    res = []
    [res.append(i) for i in lst if i not in res]
    return res


def uniq_2(lst):
    return sorted(set(lst), key=lst.index)


def uniq_3(lst):
    return list(dict.fromkeys(lst))


def uniq_4(lst):
    nl = []
    for i in lst:
        if i not in nl:
            nl.append(i)
    return nl


def gen_rnd_lst(n: int) -> list:
    return [random.randint(0, n // 2) for _ in range(n)]


lst = gen_rnd_lst(10)
# for f in (uniq_3,):
#     test = define_speed(f)
#     test(lst)
