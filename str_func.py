def get_uppercase_phrase():
    '''Делает буквы заглавными'''
    phrase = input('Введите фразу или предложение: ')
    return phrase.upper()


def get_first_worldletter_up():
    '''Повышает регистр первой буквы каждого слова'''
    phrase = input('Введите фразу или предложение: ')
    return phrase.title()
