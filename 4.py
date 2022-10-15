def my_func(x, y):
    res = 1
    ext = y * (-1)
    for op in range(0, ext):
        res = res / x
    return res


def my_func2(x, y):
    res = x ** y
    return res


x = float(input("x: "))
y = int(input("y: "))
res = my_func(x, y)
res2 = my_func2(x, y)
print(res)
print(res2)
