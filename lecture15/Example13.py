def test():
    a = [5, 4, 3, 1, 7, 16]
    even_list = list(map(lambda x: True if x % 2 == 0 else False, a))
    print(even_list.count(True))
    print(even_list.count(False))

if __name__ == '__main__':
    test()

