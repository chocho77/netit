import matplotlib.pyplot as plt
import numpy as np

def main_func():
    fig, axes = plt.subplots(2,2, figsize=(8, 8))
    colors = ["g", "b", "r", "y"]
    marker = ["o", "^", "x", "*"]
    for i, ax in enumerate(axes.reshape(4)):
        ax.plot(np.random.randint(0,10, 10), np.random.randint(5,20, 10))
    

    plt.show()

if __name__ == '__main__':
    main_func()

