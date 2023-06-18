def foo(word: str) -> str:
    """
    Docstring
    Возвращает слово с заглавных букв
    :param word:
    :return:
    """
    return word.upper()

def foo_2(word: str) ->str:
    """

    :param word:
    :return:
    """
    word_list = word.split()
    result = []
    for word in word_list:
        result.append(word.capitalize())
    return ' '.join(result)
