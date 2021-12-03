import unittest
import task2


class MyTestCase(unittest.TestCase):
    def test_rates(self):
        test_values = [str(i) for i in open('task1test.txt', 'r')]
        test_answer = task2.calculate_rates(test_values)
        answer = 230
        self.assertEqual(answer, test_answer)


if __name__ == '__main__':
    unittest.main()
