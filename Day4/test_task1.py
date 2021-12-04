import unittest
import task1


class MyTestCase(unittest.TestCase):
    def test_task1(self):
        answer = 4512
        with open('task1testinput.txt', 'r') as f:
            values = f.readline()
            values = values[:-1]  # get rid of \n
            values = values.split(",")
            game_boards = [i.split() for i in f if i != "\n"]
            final_board = task1.bingo(values, game_boards)
            result = task1.calculate_result(final_board)
        self.assertEqual(result, answer)

    def test_horizontal(self):
        board = [['Y', 'Y', 'Y', 'Y', '4'],
                 ['Y', '77', 'Y', 'Y', 'Y'],
                 ['Y', '54', '17', 'Y', '45'],
                 ['Y', '89', '62', 'Y', 'Y'],
                 ['Y', '98', '31', 'Y', '7']]
        self.assertTrue(task1.checkys(board))

if __name__ == '__main__':
    unittest.main()
