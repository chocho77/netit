def test():
    with open("content.txt", "r") as f:
        content = f.read(4)
        content_one = f.read(6)
        content_two = f.read(8)
    print(content)
    print(content_one)
    print(content_two)


if __name__ == '__main__':
    test()