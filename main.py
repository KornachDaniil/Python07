import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# График в 2D
x = np.arange(-2, 2.01, 0.01)
y1 = x ** 2
y2 = x ** 0.5

fig = plt.figure(figsize=(14, 7))  # Установка размера фигур

# Первый подграфик - график в 2D (парабола)
ax1 = fig.add_subplot(1, 2, 1)  # Добавление первого подграфика
ax1.plot(x, y1, label='y1=x^2')
ax1.plot(x, y2, label='y2=x^0.5')
ax1.fill_between(x, y1, y2, where=((x > 0) & (x < 1)), color='red', alpha=0.5)  # Закрашиваем пересечение
ax1.legend()

# Второй подграфик - график в 3D (сфера)
ax2 = fig.add_subplot(1, 2, 2, projection='3d')  # Добавление второго подграфика в 3D

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

x = 5 * np.outer(np.cos(u), np.sin(v))
y = 5 * np.outer(np.sin(u), np.sin(v))
z = 5 * np.outer(np.ones(np.size(u)), np.cos(v))

ax2.plot_surface(x, y, z, rstride=4, cstride=4, color='cyan')  # Строит сферу на втором графе

plt.show()
