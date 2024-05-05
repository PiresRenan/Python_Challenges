import unittest
from unittest.mock import patch
from io import StringIO
from controller.tts_controller import TextToSpeechController


class TestTextToSpeechController(unittest.TestCase):
    def setUp(self):
        self.controller = TextToSpeechController()

    @patch('builtins.input', side_effect=['Hello, world!'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_convert_text_to_speech(self, mock_stdout, mock_input):
        self.controller.convert_text_to_speech()
        self.assertEqual(mock_stdout.getvalue().strip(), "Fala gerada:\nHello, world!")


if __name__ == '__main__':
    unittest.main()