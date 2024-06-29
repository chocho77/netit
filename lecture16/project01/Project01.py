from ui import print_user_options, take_user_input
from validation import is_main_menu_input_valid

if __name__ == '__main__':
    print("Automotive inventory")
    while True:
        print_user_options()
        user_input = take_user_input()
        if is_main_menu_input_valid(user_input):
            print(f"User chose {user_input}")
        else:
            print("Wrong options")
    
    # while True:
       # print_user_options
       # user_input = take_user_input()
       # map_user_input(user_input)
