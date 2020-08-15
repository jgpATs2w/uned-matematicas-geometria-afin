from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

x = np.linspace(-2,2,100)
y = np.linspace(-2,2,100)

x, y = np.meshgrid(x,y)


def f(x, y):
    return 1 - x - y;

z = f(x,y)

ax = plt.axes(projection='3d')
ax.plot_surface(x,y,z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')


plt.show()