import unittest
from database import add_vehicle, get_db, clear_db, delete_vehicle, view_vehicle, update_vehicle

class MyTestCase(unittest.TestCase):
    
    def test_add_vehicle(self):
        self.assertEqual(get_db(), [])
        add_vehicle("BMW", "X5", 2000, "green", 300_000)
        self.assertEqual(get_db(), [("BMW", "X5", 2000, "green", 300_000)])
        clear_db()
        self.assertEqual(get_db(), [])
    
    def test_delete_vehicle(self):
        add_vehicle("BMW", "X5", 2000, "green", 300_000)
        delete_vehicle(0)
        self.assertEqual(get_db(), [])
    
    def test_view_vehicle(self):
        clear_db()
        add_vehicle("BMW", "X5", 2000, "green", 300_000)
        vehicle_data = view_vehicle(0)
        self.assertEqual(vehicle_data[0], "BMW")
        self.assertEqual(vehicle_data[1], "X5")
        self.assertEqual(vehicle_data[2], 2000)
        self.assertEqual(vehicle_data[3], "green")
        self.assertEqual(vehicle_data[4], 300_000)

    def test_update_vehicle(self):
        clear_db()
        add_vehicle("BMW", "X5", 2000, "green", 300_000)
        update_vehicle(0, "BMW1", "X51", 20001, "green1", 300_0001)
        vehicle_data = view_vehicle(0)
        self.assertEqual(vehicle_data[0], "BMW1")
        self.assertEqual(vehicle_data[1], "X51")
        self.assertEqual(vehicle_data[2], 20001)
        self.assertEqual(vehicle_data[3], "green1")
        self.assertEqual(vehicle_data[4], 300_0001)








if __name__ == '__main__':
    unittest.main()


