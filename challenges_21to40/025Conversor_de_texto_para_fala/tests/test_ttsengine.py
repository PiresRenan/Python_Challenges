import unittest

from text_to_speech.tts_engine import TTSEngine


class TestTTSEngine(unittest.TestCase):
    def setUp(self):
        self.tts_engine = TTSEngine()

    def test_convert_text_to_speech(self):
        text = "Teste, alo! Hello, World"
        self.tts_engine.convert_text_to_speech(text)


if __name__ == '__main__':
    unittest.main()
