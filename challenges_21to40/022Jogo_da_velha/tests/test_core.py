import unittest

from core.game import Game


class TestCore(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_valid_move(self):
        self.assertTrue(self.game.is_valid_move(0, 0))
        self.game.board = [['X', '', ''], ['', '', ''], ['', '', '']]
        self.assertFalse(self.game.is_valid_move(0, 0))

        self.assertFalse(self.game.is_valid_move(3, 3))

    def test_make_valid_move(self):
        self.assertTrue(self.game.make_move(0, 0))
        self.assertEqual(self.game.board[0][0], 'X')

        self.assertTrue(self.game.make_move(1, 1))
        self.assertEqual(self.game.board[1][1], 'O')

    def test_make_invalid_move(self):
        self.assertTrue(self.game.make_move(0, 0))
        self.assertFalse(self.game.make_move(0, 0))
        self.assertFalse(self.game.make_move(3, 3))

    def test_check_winner_horizontal(self):
        self.game.board = [
            ['X', 'X', 'X'],
            ['O', 'O', ''],
            ['', '', '']
        ]
        self.assertTrue(self.game.check_winner())
        self.game.board = [
            ['O', 'O', ''],
            ['', '', ''],
            ['X', 'X', 'X']
        ]
        self.assertTrue(self.game.check_winner())

    def test_check_winner_vertical(self):
        self.game.board = [
            ['X', 'O', ''],
            ['X', 'O', ''],
            ['X', '', '']
        ]
        self.assertTrue(self.game.check_winner())
        self.game.board = [
            ['', '', 'X'],
            ['', 'O', 'X'],
            ['', '', 'X']
        ]
        self.assertTrue(self.game.check_winner())

    def test_check_winner_diagonal(self):
        self.game.board = [
            ['X', '', ''],
            ['', 'X', ''],
            ['', '', 'X']
        ]
        self.assertTrue(self.game.check_winner())
        self.game.board = [
            ['', '', 'O'],
            ['', 'O', ''],
            ['O', '', '']
        ]
        self.assertTrue(self.game.check_winner())


if __name__ == '__main__':
    unittest.main()
