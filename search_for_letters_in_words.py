def count_letter(words, letter):
    x = 0
    for word in words:
        for letters in word:
            if letters == letter:
                x = x + 1
    return print(x)


def count_words(word, letter):
    words = []
    for i in word:
        for letters in i:
            if letters == letter:
                words.append(i)
    return print(len(set(words)))


a = input("Введите слова: ").split()
b = input("Введите искомую букву: ")
count_words(a, b)
