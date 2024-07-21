from typing import Tuple

def is_even(x: Tuple [int, int]):
    return x[0] % 2 == 0


def main():
    l_tuple = [(2, 10), (4, 5), (1, 2), (7, 8)]
    for element in l_tuple:
        print(is_even(element))


if __name__ == '__main__':
    main()
