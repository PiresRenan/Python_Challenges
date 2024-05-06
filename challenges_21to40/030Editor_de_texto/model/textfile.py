class TextFile:
    def __init__(self, filename: str, content: str) -> None:
        self.filename = filename
        self.content = content

    def save(self, filename: str) -> None:
        with open(filename, 'w') as f:
            f.write(self.content)

    @staticmethod
    def load(filename: str) -> 'TextFile':
        with open(filename, 'r') as f:
            content = f.read()
        return TextFile(filename, content)