from pkg.calculator import *


def print_hi(name):
    print(f'Hi, {name}.')

def print_hello():
    print("Hello World.")


if __name__ == '__main__':
    print_hello()
    print_hi("Chavdar")

    sum = sum(2, 3)
    sub = sub(3, 2)
    mul = multiply(3, 4)
    div = div(6, 2)
    print(f'sum = {sum}')
    print(f'sub = {sub}')
    print(f'mul = {mul}')
    print(f'div = {div}')

    print_info()

    

