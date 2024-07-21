def is_even(x):
    return x % 2 == 0


def main():
    l = [5, 4, 3, 1, 7, 16]
    for element in l:
        print(is_even(element))


if __name__ == '__main__':
    main()

