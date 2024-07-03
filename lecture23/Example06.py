import numpy as np

def test():
    array1 = np.array([[1, 2, 3], [4, 5, 6]])
    array2 = np.array([[7, 8, 9], [10, 11, 12]])
    
    print(array1 + array2)
    print("-" * 20)

    print(array1 - array2)
    print("-" * 20)

    print(array1 * array2)
    print("-" * 20)

    print(array2 / array1)
    print("-" * 40)

    print(array1 ** array2)
    print("-" * 40)

if __name__=='__main__':
    test()
