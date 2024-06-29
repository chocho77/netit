from sys import exit

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
        pass
    elif user_input == 6:
        exit(0)
    else:
        print("Unknown option")

   