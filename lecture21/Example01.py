def test():
    f = open("data.txt", "r")
    data = f.read()
    f.close()
    print(data)


if __name__ == '__main__':
    test()


