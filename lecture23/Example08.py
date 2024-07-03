import numpy as np

def test():
    array1 = np.array([[10, 20, 30], [40, 50, 60]])
    
    print(np.sin(array1))
    print("-" * 40)

    print(np.cos(array1))
    print("-" * 40)

    print(np.tan(array1))
    print("-" * 40)

    print(np.sqrt(array1))
    print("-" * 40)

    print(np.exp(array1))
    print("-" * 40)

    print(np.log10(array1))
    print("-" * 40)

if __name__ == '__main__':
    test()

