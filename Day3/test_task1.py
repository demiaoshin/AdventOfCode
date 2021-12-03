import unittest
import task1


class MyTestCase(unittest.TestCase):
    def test_rates(self):
        test_values = [str(i) for i in open('task1test.txt', 'r')]
        answer = 198
        test_answer = task1.calculate_rates(test_values)
        self.assertEqual(test_answer, answer)


if __name__ == '__main__':
    unittest.main()
