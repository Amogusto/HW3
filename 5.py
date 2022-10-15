def my_sum(string, sum):
    br = False
    spisok = string.split(' ')
    for el in spisok:
        try:
            el = int(el)
            sum += el
        except:
            if el == "!":
                br = True
                break
            else:
                print("Неверный формат данных")
    return [sum, br]


sum = 0
while True:
    string = input("Введите строку чискл (! если хотите прекратить ввод)")
    sum, br = my_sum(string, sum)
    print(sum)
    if br == True:
        break
