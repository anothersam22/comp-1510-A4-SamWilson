from unittest import TestCase
from unittest.mock import patch
from game import make_character


class TestMakeCharacter(TestCase):

    @patch('random.randint', return_value=[5, 5])
    def test_make_character(self, mock_output):
        self.assertEqual(make_character("Dave"), {'Brain Power': 0,
                                                  'Level': 1,
                                                  'Level Tracker': [],
                                                  'Name': 'Dave',
                                                  'X-Coordinate': [5, 5],
                                                  'Y-Coordinate': [5, 5]})

    @patch('random.randint', return_value=[0, 9])
    def test_make_character_different_x_y(self, mock_output):
        self.assertEqual(make_character("Dave"), {'Brain Power': 0,
                                                  'Level': 1,
                                                  'Level Tracker': [],
                                                  'Name': 'Dave',
                                                  'X-Coordinate': [0, 9],
                                                  'Y-Coordinate': [0, 9]})
