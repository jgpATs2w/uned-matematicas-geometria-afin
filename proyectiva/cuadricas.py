from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

x = np.linspace(-20,20,100)
y = np.linspace(-20,20,100)

x, y = np.meshgrid(x,y)


def elipsoide(x, y):
    return np.sqrt(1 - x**2 - y**2)
def hiperboloide_eliptico(x, y):
    return np.sqrt(1 + x**2 + y**2)

z = hiperboloide_eliptico(x,y)

ax = plt.axes(projection='3d')
ax.plot_surface(x,y,z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')


plt.show()