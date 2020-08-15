import numpy as np
from sympy import Matrix, init_printing, eye, symbols, simplify, sqrt, pprint, Point
from sympy.plotting import plot
init_printing(use_unicode=True)

x1, x2 = symbols('x1 x2')
a = Point([1,0])
b = Point(3,-2)
a.distance(b)

J = Matrix(3,3,[1,0,0, a.distance(b),1,0, 0,0,-1])
M = Matrix(3,3,[1,0,0, a.distance(b),1,0, 0,0,-1])

pprint(M*Matrix([1,1,0]))








