from sympy import symbols
from sympy.plotting import plot3d

x1, x2, x3 = symbols('x1 x2 x3')

plot3d(x1+x2+x3-1, (x1, -5, 5), (x2, -5, 5), (x3, -5, 5))