import numpy as np
from sympy import Matrix, init_printing, eye, symbols, simplify, sqrt, pprint, Point
from sympy.plotting import plot
init_printing(use_unicode=True)

M = Matrix(4,4,[1,0,0,0,
            1,1/2,sqrt(3)/2,0,
            -1,-sqrt(3)/2,1/2,0,
            2,0,0,1])

Md = Matrix(4,4,[1,0,0,0,
            1,1/2,sqrt(3)/2,0,
            -1,-sqrt(3)/2,1/2,0,
            2,0,0,1])
Md.col_del(0)
Md.row_del(0)

pprint(M.jordan_form())








