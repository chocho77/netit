import unittest

def sum_two_numbers(a: int,b: int):
    return a + b

def multiply_two_numbers(a: int, b: int):
    return a * b


# manual testing function logic

# print(sum_two_numbers(2,3)==6)  # False
# print(sum_two_numbers(2,3)==5)  # True

class MyTestCase(unittest.TestCase):
    def test_sum_two_numbers(self):
        self.assertEqual(sum_two_numbers(3,2), 5)
        self.assertEqual(sum_two_numbers(9,11), 20)
    
    def test_multiply_two_numbers(self):
        self.assertEqual(multiply_two_numbers(3,2), 6)

if __name__ == '__main__':
    unittest.main()

