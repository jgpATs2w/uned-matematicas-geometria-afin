from sympy import symbols
from sympy.geometry import Point, Triangle, intersection

a, b = symbols("a,b", positive=True)

x = Point(0, 0)
y = Point(a, 0)
z = Point(2*a, b)
t = Triangle(x, y, z)

print(t.area)

print(t.medians[x])

print(intersection(t.medians[x], t.medians[y], t.medians[z]))