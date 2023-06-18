def foo(word: str) -> str:
    """
    Возвращает слово с заглавных букв
    :param word:
    :return:
    """
    return word.upper()

def foo_2(word: str) -> str:
    """
    Возвращает все слова с заглавной буквы
    :param word:
    :return:
    """
    words_list = word.split()
    result =[]
    for word in words_list:
        result.append(word.capitalize())
    return ' '.join(result)

