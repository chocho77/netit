import numpy as np
def test():
    a = np.arange(15).reshape(3, 5)

    print(a)
    print()
    print(a.shape)
    print()
    print(a.ndim)
    print()
    print(a.dtype.name)
    print()
    print(a.itemsize)
    print()

    print(a.size)
    print()
    print(type(a))

if __name__ == '__main__':
    test()

