import numpy as np

def test():
    array1 = np.array([[10, 20, 30], [40, 50, 60]])

    print(array1 + 2)
    print("-" * 20)

    print(array1 - 5)
    print("-" * 20)

    print(array1 * 2)
    print("-" * 20)

    print(array1 / 5)
    print("-" * 20)

    print(array1 ** 2)
    print("-" * 20)

if __name__ == '__main__':
    test()
