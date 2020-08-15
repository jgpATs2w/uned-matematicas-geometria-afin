from sympy import symbols

x, y, z = symbols('x y z')
expr = 2*x + y
print( expr.subs(x, 2).subs(y,3) )