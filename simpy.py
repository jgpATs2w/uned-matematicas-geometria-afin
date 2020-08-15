from sympy import *
from sympy.geometry import *
x = Point(0, 0)
y = Point(1, 1)
z = Point(2, 2)
zp = Point(1, 0)
Point.is_collinear(x, y, z)

Point.is_collinear(x, y, zp)

t = Triangle(zp, y, x)
t.area

t.medians[x]
Segment2D(Point2D(0, 0), Point2D(1, 1/2))
m = t.medians
intersection(m[x], m[y], m[zp])
[Point2D(2/3, 1/3)]
c = Circle(x, 5)
l = Line(Point(5, -5), Point(5, 5))
c.is_tangent(l) # is l tangent to c?

l = Line(x, y)
c.is_tangent(l) # is l tangent to c?

x, y, z = symbols('x y z')
expr = 2*x + y
expr2 = expr.subs(x, 2)
expr2