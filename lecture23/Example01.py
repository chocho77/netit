import numpy as np

# https://numpy.org/

def test():
    # Arrays with arange
    array1d = np.arange(5)   # 1 row and 5 columns
    print(array1d)

    array1d = np.arange(0, 12, 2) # 1 row and 6 columns
    print(array1d)

    array2d = np.arange(0, 12, 2).reshape(2, 3) # 2 rows 3 columns
    print(array2d)

    array3d = np.arange(9).reshape(3, 3) # 3 rows and columns
    print(array3d)
    

if __name__ == '__main__':
    test()
