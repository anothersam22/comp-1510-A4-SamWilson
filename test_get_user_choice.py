from unittest import TestCase
from unittest.mock import patch

from game import get_user_choice


class TestGetUserChoice(TestCase):
    @patch('builtins.input', side_effect=["1"])
    def test_get_user_choice_up(self, mock_input):
        self.assertEqual(get_user_choice(["up", "down", "left", "right"]), 0)

    @patch('builtins.input', side_effect=["2"])
    def test_get_user_choice_down(self, mock_input):
        self.assertEqual(get_user_choice(["up", "down", "left", "right"]), 1)

    @patch('builtins.input', side_effect=["3"])
    def test_get_user_choice_left(self, mock_input):
        self.assertEqual(get_user_choice(["up", "down", "left", "right"]), 2)

    @patch('builtins.input', side_effect=["4"])
    def test_get_user_choice_right(self, mock_input):
        self.assertEqual(get_user_choice(["up", "down", "left", "right"]), 3)
