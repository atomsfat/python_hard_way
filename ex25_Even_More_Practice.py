def break_words(stuff):
    """This is will break up words for us"""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sorts the words"""
    return sorted(words)


def print_first_words(words):
    """print the first word after popping off"""
    word = words.pop(0)
    print(word)


def print_last_words(words):
    """print the last owrds after popping off"""
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    """takes in a full sentence and return the sorted words"""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """prints the first and last words of the sentence"""
    words = break_words(sentence)
    print_first_words(words)
    print_last_words(words)


def print_first_and_last_sorted(sentence):
    """sort the words then prints the first and last one"""
    words = sort_sentence(sentence)
    print_first_words(words)
    print_last_words(words)
