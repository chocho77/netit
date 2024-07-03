import numpy as np

def test():
    # arrays with logspace

    thearray = np.logspace(5, 10, base=10000000.0, dtype=float)
    print(thearray)

if __name__ == '__main__':
    test()

