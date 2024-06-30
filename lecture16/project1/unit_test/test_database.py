import unittest
from project01.database import add_vehicle_to_db


def sum_two_numbers(a, b):
    return a + b


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(sum_two_numbers(2,2), 4)
        self.assertEqual(sum_two_numbers(2,2), 0)



if __name__ == '__main__':
    unittest.main()


