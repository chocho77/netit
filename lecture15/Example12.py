def test():
    a = [5, 4, 3, 1, 7, 16]
    even = tuple(filter(lambda x: x % 2 == 0, a))
    print(len(even))
    odd = tuple(filter(lambda x: x % 2 != 0, a))
    print(len(odd))

if __name__ == '__main__':
    test()

