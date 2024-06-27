def print_res():
    a = [5, 4, 3, 1, 7, 16]
    b = [5, 4, 3, 1, 7]

    for x in filter(lambda el: el in b, a):
        print(x)

    print()

    result = tuple(filter(lambda el: el in b, a))
    print(result)


if __name__ == '__main__':
    print_res()



