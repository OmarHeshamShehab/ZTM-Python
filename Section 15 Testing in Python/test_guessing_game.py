import unittest

import Guessing_game


class TestGame(unittest.TestCase):
    def test_input(self):
        result = Guessing_game.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = Guessing_game.run_guess(5, 6)
        self.assertFalse(result)

    def test_input_out_of_range(self):
        result = Guessing_game.run_guess(5, 15)
        self.assertFalse(result)

    def test_input_string(self):
        result = Guessing_game.run_guess(5, "15")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
