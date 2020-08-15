import numpy as np
from sympy import Matrix, init_printing, eye, symbols, simplify
init_printing(use_unicode=True)

M = Matrix(4,4, [1,0,0,0, 1,1,0,-1, 1,0,-1,0, 1,1,0,1])
F = Matrix(3,3, [1,0,-1, 0,-1,0, 1,0,1])
t = symbols('t')
FtI = F - t*eye(3)
P, J = F.jordan_form()

#print(simplify(FtI.charpoly()))
print(F.eigenvals())
print(J)