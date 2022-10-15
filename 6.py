def int_func(word):
    res = []
    word2 = ""
    for let in word:
        res.append(let)
        res[0] = res[0].upper()
    for let in res:
        word2 += let
    return word2


word = input("Введите слово: ")
res = int_func(word)
print(res)
