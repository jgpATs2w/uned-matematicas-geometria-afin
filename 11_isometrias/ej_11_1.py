import numpy as np
from sympy import Matrix, init_printing, eye, symbols, simplify, sqrt, pprint
from fractions import Fraction
init_printing(use_unicode=True)

M = Matrix(3,3,[1,0,0, 9/2,-1/2,sqrt(3)/2, sqrt(3)/2,sqrt(3)/2,1/2])
Md = Matrix(2,2,[-1/2,sqrt(3)/2, sqrt(3)/2,1/2])
N = Matrix(M-eye(3))
pprint(Md.charpoly())
print(N.rank())

x1, x2 = symbols('x1 x2')
O=Matrix(N**2 * Matrix(3,1,[1,x1,x2]))
pprint(O.rowspace())

punto_eje = Matrix([1,2,0])
D = Matrix(M * punto_eje - punto_eje)
print("mu = %.2f" % D.norm())



