def test():
    a = [2,3,4,5]
    b = [2,3,4]

    result = [el for el in a if el in b]
    print(result)

if __name__ == '__main__':
    test()

