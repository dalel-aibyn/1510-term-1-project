from unittest import TestCase
import game


class Test(TestCase):
    def test_get_encounter_probability_entrance_low_level(self):
        character = {"level": 1.2, "opponent_encounter_cooldown": 3}
        expected_probability = 2

        actual_probability = game.get_encounter_probability(character, "Entrance")

        self.assertEqual(expected_probability, actual_probability)

    def test_get_encounter_probability_entrance_high_level(self):
        character = {"level": 8.7, "opponent_encounter_cooldown": 4}
        expected_probability = 5

        actual_probability = game.get_encounter_probability(character, "Entrance")

        self.assertEqual(expected_probability, actual_probability)

    def test_get_encounter_probability_number_theory_low_level(self):
        character = {"level": 1.5, "opponent_encounter_cooldown": 4}
        expected_probability = 1

        actual_probability = game.get_encounter_probability(character, "Number Theory")

        self.assertEqual(expected_probability, actual_probability)

    def test_get_encounter_probability_algebra_mid_level(self):
        character = {"level": 4.2, "opponent_encounter_cooldown": 3}
        expected_probability = 2

        actual_probability = game.get_encounter_probability(character, "Algebra")

        self.assertEqual(expected_probability, actual_probability)

    def test_get_encounter_probability_calculus_high_cooldown(self):
        character = {"level": 3.8, "opponent_encounter_cooldown": 5}
        expected_probability = 2

        actual_probability = game.get_encounter_probability(character, "Calculus")

        self.assertEqual(expected_probability, actual_probability)

    def test_get_encounter_probability_arithmetics_zero_cooldown(self):
        character = {"level": 2.5, "opponent_encounter_cooldown": 1}
        expected_probability = 1

        actual_probability = game.get_encounter_probability(character, "Arithmetics")

        self.assertEqual(expected_probability, actual_probability)

    def test_get_encounter_probability_all_areas_same_character(self):
        character = {"level": 6.8, "opponent_encounter_cooldown": 3}
        expected_probabilities = {
            "Entrance": 5,
            "Arithmetics": 4,
            "Algebra": 3,
            "Calculus": 2,
            "Number Theory": 1
        }

        for area, expected in expected_probabilities.items():
            actual = game.get_encounter_probability(character, area)
            self.assertEqual(expected, actual, f"Failed for area: {area}")
