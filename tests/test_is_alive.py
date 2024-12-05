from unittest import TestCase
import game


class Test(TestCase):
    def test_is_alive_high_mood(self):
        character = {"mood": 20}
        expected = True

        actual = game.is_alive(character)

        self.assertEqual(expected, actual)

    def test_is_alive_low_mood(self):
        character = {"mood": 1}
        expected = True

        actual = game.is_alive(character)

        self.assertEqual(expected, actual)

    def test_is_alive_zero_mood(self):
        character = {"mood": 0}
        expected = False

        actual = game.is_alive(character)

        self.assertEqual(expected, actual)

    def test_is_alive_negative_mood(self):
        character = {"mood": -69}
        expected = False

        actual = game.is_alive(character)

        self.assertEqual(expected, actual)
