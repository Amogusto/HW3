def int_func(word):
    res = []
    word2 = ""
    for let in word:
        res.append(let)
        res[0] = res[0].upper()
    for let in res:
        word2 += let
    return word2


sentence = input("Введите слово: ")
sentence2 = ""
words = sentence.split(" ")
for word in words:
    word = int_func(word)
    sentence2 += word
    sentence2 += " "
print(sentence2)
