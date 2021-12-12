import unittest
import task1


class MyTestCase(unittest.TestCase):
    def test_task1(self):
        new_vals = [i.split(",") for i in open('testtask1.txt', 'r')]
        new_vals = new_vals[0]
        final_val = task1.fishcount(new_vals)
        self.assertEqual(final_val, 26984457539)


if __name__ == '__main__':
    unittest.main()
