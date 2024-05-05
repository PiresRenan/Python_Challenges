from text_to_speech.tts_engine import TTSEngine
from user_interface.cli_view import CommandLineInterface


class TextToSpeechController:
    def __init__(self):
        self.tts_engine = TTSEngine()
        self.cli_interface = CommandLineInterface()

    def convert_text_to_speech(self, text):
        speech = self.tts_engine.convert_text_to_speech(text)
        self.cli_interface.display_output(speech)
