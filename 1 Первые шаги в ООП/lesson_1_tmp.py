a = [1, 2, 3, 4, 5, 6, 7]

n = 2
print(list(zip(*[iter(a)] * n)))

# x = iter([1, 2, 3, 4, 5, 6, 7, 8, 9])
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(list, zip(x[::2], x[1::2]))))

# print([tuple(a[i:i + n]) for i in range(0, len(a), n) if len(a[i:i + n])])


unic_key = dict.fromkeys(map(lambda x: tuple(sorted(x)), ((1,2), (2,1))), None)
print(unic_key)