import unittest
from database import add_vehicle_to_db, get_db, clear_db

class MyTestCase(unittest.TestCase):
    
    def test_add_vehicle(self):
        self.assertEquals(get_db(), [])
        add_vehicle_to_db("BMW", "X5", 2000, "green", 300_000)
        self.assertEqual(get_db(), [("BMW", "X5", 2000, "green", 300_000)])
        clear_db()
        self.assertEqual(get_db(), [])


if __name__ == '__main__':
    unittest.main()

