# updating using where()
import numpy as np

def test():
    
    before = np.array([[1, 2, 3], [4, 5, 6]])

    # If element is less than 4, mul by 2 else by 3
    after = np.where(before < 4, before * 2, before * 3)
    print(after)


if __name__ == '__main__':
    test()

