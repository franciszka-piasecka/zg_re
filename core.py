import string


def normalize_words(words):
    punctuation_translation = str.maketrans('', '', string.punctuation)
    cleaned_words = words.translate(punctuation_translation)
    return (word.lower() for word in cleaned_words.split())


def find_shortest_distance(first_word, second_word, words):
    first_normalized_word = first_word.lower()
    second_normalized_word = second_word.lower()
    normalized_words = normalize_words(words)
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
        raise ValueError()
    last_index = i
    # An impossible value
    shortest_distance = len(words) + 1
    for i, word in enumerated_words:
        if word == sought_word:
            sought_word, found_word = found_word, sought_word
            shortest_distance = min(shortest_distance, i - last_index - 1)
            last_index = i
    return shortest_distance
