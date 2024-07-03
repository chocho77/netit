import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [4, 2, 5, 6, 4]
x1 = [4, 6, 7, 8]
y1 = [2, 4, 6, 1]

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.set_xlabel("Hello")
ax2.set_ylabel("Hello again")
ax1.set_xlim(-5,  10)
plt.tight_layout()
ax1.plot(x, y)
ax2.plot(x1, y1)
plt.show()
