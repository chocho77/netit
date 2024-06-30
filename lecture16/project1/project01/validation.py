from vehicle_management import MAIN_MENU_OPTIONS


def is_main_menu_input_valid(user_input: str)-> bool:
    if not user_input.isdigit():
        return False
    user_input_num = int(user_input) - 1
    if user_input_num < 0 or user_input_num >= len(MAIN_MENU_OPTIONS):
        return False
    return True

    
