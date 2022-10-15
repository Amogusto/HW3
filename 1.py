def my_div(a, b):
    try:
        res = a / b
        return res
    except ZeroDivisionError:
        print("Ошибка деления на ноль")


a = int(input("Введите делимое"))
b = int(input("Введите делитель"))
res = my_div(a, b)
print(res)
