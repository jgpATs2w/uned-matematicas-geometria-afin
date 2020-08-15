import numpy as np
from sympy import Matrix, init_printing, eye, zeros, symbols, simplify, sqrt, pprint, Point, linsolve, solve
from sympy.plotting import plot
init_printing(use_unicode=True)

M = Matrix(4,4,[1,0,0,0,
            1,0,-1,0,
            1,1,0,0,
            1,0,0,-1])

Md = Matrix(M)
Md.col_del(0)
Md.row_del(0)

# del polinomio caract. se observa que es ( rotación pi/2 ) o (reflexión)
pprint(M.charpoly())
pprint(M.jordan_form())
pprint(Md.jordan_form())

print("vectores invariantes")
pprint(Matrix(Md-eye(3)).nullspace())

# hayar punto fijo
x1,x2, x3 = symbols('x1 x2 x3')
A = Matrix(M-eye(4))
X = Matrix([1,x1,x2,x3])
B = zeros(4,1)

system = A,b = A, B
pprint(linsolve(system, 1,x1,x2,x3))








