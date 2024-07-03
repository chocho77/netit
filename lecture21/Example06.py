def test():
    try:
        with open("nodata.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("File does not exist")

if __name__ == '__main__':
    test()

