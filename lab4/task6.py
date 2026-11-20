# Обратный порядок слов: Напишите функцию, которая рекурсивно меняет порядок слов в заданной строке на обратный.

def reverse_words(text):
    parts = text.split(maxsplit=1)

    if len(parts) == 0:
        return ""
    if len(parts) == 1:
        return parts[0]

    return reverse_words(parts[1]) + " " + parts[0]

if __name__ == "__main__":
    text = input("Введите строку: ")
    print("Обратный порядок слов:", reverse_words(text.strip()))