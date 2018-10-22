import functools
import string


def normalize_words(words):
    punctuation_translation = str.maketrans('', '', string.punctuation)
    cleaned_words = words.translate(punctuation_translation)
    return (word.lower() for word in cleaned_words.split())


def find_shortest_distance(first_word, second_word, words):
    first_normalized_word = first_word.lower()
    second_normalized_word = second_word.lower()

    def foo(total, word_tuple):
        index, word = word_tuple
        if word == first_normalized_word:
            total['first_index'] = index
        elif word == second_normalized_word:
            total['second_index'] = index
        total['shortest_distance'] = min(
            total['shortest_distance'], abs(total['first_index'] - total['second_index']) - 1
        )
        return total

    normalized_words = normalize_words(words)
    initial_distance = len(words) + 1
    result = functools.reduce(foo, enumerate(normalized_words), {
        'first_index': initial_distance, 'second_index': -initial_distance, 'shortest_distance': initial_distance
    })
    return result['shortest_distance']
