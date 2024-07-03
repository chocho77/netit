import matplotlib.pyplot as plt
x = [0, 1, 2, 4, 3]
y = [1, 5, 3, 4, 5]
plt.title("Data")
plt.xlabel("X")
plt.ylabel("Y")
plt.xlim(0, 3)
plt.ylim(0,8)
plt.plot(x, y, "go-")   # plot_format {color}{marker}{line}
plt.show()