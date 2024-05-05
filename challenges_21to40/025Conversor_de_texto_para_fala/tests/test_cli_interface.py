import unittest
from unittest.mock import patch
from io import StringIO
from user_interface.cli_view import CommandLineInterface


class TestCommandLineInterface(unittest.TestCase):
    def setUp(self):
        self.cli = CommandLineInterface()

    @patch('builtins.input', side_effect=['Hello, world!'])
    def test_get_user_input(self, mock_input):
        user_input = self.cli.get_user_input()
        self.assertEqual(user_input, 'Hello, world!')

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_output(self, mock_stdout):
        speech = "This is a test speech."
        self.cli.display_output(speech)
        self.assertEqual(mock_stdout.getvalue().strip(), "Fala gerada:\nThis is a test speech.")


if __name__ == '__main__':
    unittest.main()
