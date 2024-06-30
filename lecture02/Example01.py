def test(value: int)->None:
    x = value
    if x > 0:
        print("x is greater than zero.")
    elif x == 0:
        print("x is equal zero.")
    else:
        print("x is less than zero.")


if __name__ == '__main__':
    test(-1)
    test(0)
    test(1)




