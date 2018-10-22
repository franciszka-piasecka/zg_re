import unittest
import core


class TestFindShortestDistance(unittest.TestCase):
    def test_find_shortest_distance_valid_words(self):
        words = 'We do value and reward motivation in our development team. Development is a key skill for a DevOp.'
        result = core.find_shortest_distance('motivation', 'development', words)
        self.assertEqual(result, 2)

    def test_find_shortest_distance_valid_words_reverse_order(self):
        words = 'We do value and reward motivation in our development team. Development is a key skill for a DevOp.'
        result = core.find_shortest_distance('development', 'motivation', words)
        self.assertEqual(result, 2)

    def test_find_shortest_distance_valid_words_zero_distance(self):
        words = 'We do value and reward motivation in our development team. Development is a key skill for a DevOp.'
        result = core.find_shortest_distance('do', 'value', words)
        self.assertEqual(result, 0)

    def test_find_shortest_distance_valid_words_max_distance(self):
        words = 'We do value and reward motivation in our development team. Development is a key skill for a DevOp.'
        result = core.find_shortest_distance('We', 'DevOp', words)
        self.assertEqual(result, 16)

    def test_find_shortest_distance_valid_words_case_insensitive(self):
        words = 'We do value and reward motivation in our development team. Development is a key skill for a DevOp.'
        result = core.find_shortest_distance('we', 'devop', words)
        self.assertEqual(result, 16)

    def test_find_shortest_distance_valid_words_with_punctuation(self):
        words = 'We do value and reward motivation in our development team. Development is a key skill for a DevOp.'
        result = core.find_shortest_distance('reward', 'team', words)
        self.assertEqual(result, 4)

    def test_find_shortest_distance_one_invalid_word(self):
        words = 'We do value and reward motivation in our development team. Development is a key skill for a DevOp.'
        with self.assertRaises(ValueError):
            core.find_shortest_distance('invalid', 'motivation', words)

    def test_find_shortest_distance_one_invalid_word_reverse_order(self):
        words = 'We do value and reward motivation in our development team. Development is a key skill for a DevOp.'
        with self.assertRaises(ValueError):
            core.find_shortest_distance('motivation', 'invalid', words)

    def test_find_shortest_distance_both_invalid_words(self):
        words = 'We do value and reward motivation in our development team. Development is a key skill for a DevOp.'
        with self.assertRaises(ValueError):
            core.find_shortest_distance('invalid', 'wrong', words)
