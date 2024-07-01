from sys import exit
from typing import Tuple
from database import add_vehicle, delete_vehicle

MAIN_MENU_OPTIONS = (
      "Add vehicle to Inventory",
      "Delete vehicle from Inventory",
      "View Current Inventory",
      "Update Vehicle in Inventory",
      "Export Current Inventory",
      "Quit"
   )

def map_user_input(user_input: int):
    if user_input == 1:
        vehicle_data = take_user_add_vehicle_imput()
        # validate
        add_vehicle(*vehicle_data)
        print("Vehicle added successfully")
    elif user_input == 2:
        _id = take_user_delete_vehicle_input()
        # validate
        delete_vehicle(int(_id))
        print("Vehicle deleted successfully")
    elif user_input == 3:
        pass
        
    elif user_input == 6:
        exit(0)
    else:
        raise RuntimeError(f"Unknown main menu option {user_input}")
    
def take_user_add_vehicle_imput() \
    -> Tuple[str, str, str, str, str]:
    make = input()
    model = input()
    year = input()
    color = input()
    range = input()

    return make, model, year, color, range

def take_user_delete_vehicle_input():
    return input("Enter id")



