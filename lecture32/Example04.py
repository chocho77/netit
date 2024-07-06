def print_hello():
    print("Hello World.")

def calculate_numbers(first_number, second_number):
    return first_number + second_number

if __name__ == '__main__':
    print_hello()
    first_result = calculate_numbers(6, 8)
    print(f'first result : {first_result}')
    print_hello()
    print_hello()

    raise Exception()  # raise Exception 

    print_hello()

    print_hello()



