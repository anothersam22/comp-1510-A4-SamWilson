import io
from unittest import TestCase
from unittest.mock import patch
from game import get_user_choice


class TestGetUserChoice(TestCase):
    @patch('builtins.input', side_effect=[1, 10, 5])
    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice(self, mock_output, ):
        get_user_choice()
        self.fail()
