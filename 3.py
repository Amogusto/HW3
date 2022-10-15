def my_func(a, b, c):
    if a > b:
        if b > c:
            return a + b
        else:
            return a + c
    else:
        if a < c:
            return b + c
        else:
            return a + b


a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

res = my_func(a, b, c)
print(res)
