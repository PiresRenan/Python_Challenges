import pyttsx3


class TTSEngine:
    def __init__(self):
        self.engine = pyttsx3.init()

    def convert_text_to_speech(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
