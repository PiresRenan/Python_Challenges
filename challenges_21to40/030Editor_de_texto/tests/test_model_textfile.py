import unittest
from model.textfile import TextFile


class TestTextFile(unittest.TestCase):
    def test_save_and_load(self):
        filename = 'test.txt'
        content = 'This is a test file.'
        file = TextFile(filename, content)

        file.save(filename)
        loaded_file = TextFile.load(filename)

        self.assertEqual(content, loaded_file.content)

        import os
        os.remove('test.txt')


if __name__ == '__main__':
    unittest.main()
