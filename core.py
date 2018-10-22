import string


def get_normalized_words(words):
    punctuation_translation = str.maketrans('', '', string.punctuation)
    cleaned_words = words.translate(punctuation_translation)
    return (word.lower() for word in cleaned_words.split())


def find_shortest_distance(first_word, second_word, text):
    '''
    Finds the shortest absolute distance (in words) between first_word and second_word in text.
    Case and punctuation are ignored.
    :param first_word: str
    :param second_word: str
    :param text: str
    :return: int
    :raises: ValueError if either or both words are missing from text.
    '''
    first_normalized_word = first_word.lower()
    second_normalized_word = second_word.lower()
    normalized_words = get_normalized_words(text)
    enumerated_words = enumerate(normalized_words)
    for i, word in enumerated_words:
        if word == first_normalized_word:
            sought_word = second_normalized_word
            found_word = first_normalized_word
            break
        elif word == second_normalized_word:
            sought_word = first_normalized_word
            found_word = second_normalized_word
            break
    else:
        raise ValueError('both words missing from given string')
    last_index = i
    # An impossible value
    initial_shortest_distance = len(text) + 1
    shortest_distance = initial_shortest_distance
    for i, word in enumerated_words:
        if word == sought_word:
            sought_word, found_word = found_word, sought_word
            shortest_distance = min(shortest_distance, i - last_index - 1)
            last_index = i
    if shortest_distance != initial_shortest_distance:
        return shortest_distance
    else:
        raise ValueError(f'{sought_word} not found in given string')
