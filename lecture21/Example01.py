def test():
    f = open("data.txt", "r")
    data = f.read()
    print(data)
    f.close()


if __name__ == '__main__':
    test()


