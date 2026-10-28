# Exercise 3 - Tutorial 4 2026-2027

from sympy import *

Gs, G, R, Y = symbols('Gs, G, R, Y')

Y-(R+Y)*Gs*G

print(Y)

Y = solve(Y-(R-Y)*Gs*G, Y)

print(Y[0]/R)
