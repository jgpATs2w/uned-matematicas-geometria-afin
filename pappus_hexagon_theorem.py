from sympy import *
from sympy.geometry import *

l1 = Line(Point(0, 0), Point(5, 6))
l2 = Line(Point(0, 0), Point(2, -2))

def subs_point(l, val):
    """Take an arbitrary point and make it a fixed point."""
    t = Symbol('t', real=True)
    ap = l.arbitrary_point()
    return Point(ap.x.subs(t, val), ap.y.subs(t, val))

p11 = subs_point(l1, 5)
p12 = subs_point(l1, 6)
p13 = subs_point(l1, 11)

p21 = subs_point(l2, -1)
p22 = subs_point(l2, 2)
p23 = subs_point(l2, 13)

ll1 = Line(p11, p22)
ll2 = Line(p11, p23)
ll3 = Line(p12, p21)
ll4 = Line(p12, p23)
ll5 = Line(p13, p21)
ll6 = Line(p13, p22)

pp1 = intersection(ll1, ll3)[0]
pp2 = intersection(ll2, ll5)[0]
pp3 = intersection(ll4, ll6)[0]

print(Point.is_collinear(pp1, pp2, pp3))