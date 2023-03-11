#
# import copy
# import numpy
# from scipy.linalg import solve
# from sympy import symbols, diff, lambdify, simplify, solve, expand
# l, x = symbols('l, x')
# def myround(num):
#     return round(num, 5)
# A = [
#     [-4-l, 1, -1],
#     [2, -2-l, 3],
#     [3, 1, 3-l]
# ]
# opr = A[0][0] * A[1][1] * A[2][2]\
#       + A[0][1] * A[1][2] * A[2][0]\
#       + A[0][2] * A[1][0] * A[2][1]\
#       - A[0][2] * A[1][1] * A[2][0]\
#       - A[0][1] * A[1][0] * A[2][2]\
#       - A[0][0] * A[1][2] * A[2][1]
# opr *= -1
# print(opr)
# opr = simplify(opr)
# print(opr)
# print()
#
# df = diff(opr, l)
# print("f'(l) = ", df)
#
# solv = solve(df)
# print(f"l1 = {myround(solv[0])}\n"
#       f"l2 = {myround(solv[1])}")
# # print(float(solv[0]), float(solv[1]))
#
# f = lambdify(l, opr)
#
# f1 = lambdify(l, df)
#
# l0 = 0
# l1 = l0 - f(l0)/ f1(l0)
#
# print("Итерации:")
# print("l0 = ", myround(l0))
# print(f(l0), f1(l0), f(l0)/ f1(l0))
# print("l1 = " ,myround(l1))
# c = 2
# while abs(l1 - l0) > 0.0001:
#     l0 = l1
#     print(f(l0), f1(l0), f(l0) / f1(l0))
#     l1 = l0 - f(l0) / f1(l0)
#     print(f"l{c} = ", myround(l1))
#     c+= 1
# print()
# fl = expand(opr / (l-float(l0)))
#
# lsolv = [complex(i).real for i in solve(fl)]
# print(f"l1 = {myround(lsolv[0])}\n"
#       f"l2 = {myround(lsolv[1])}\n"
#       f"l3 = {myround(lsolv[2])}")
#
#
# A1 = copy.deepcopy(A)
# A1[0][0] = lambdify(l, A1[0][0])(lsolv[0])
# A1[1][1] = lambdify(l, A1[1][1])(lsolv[0])
# A1[2][2] = lambdify(l, A1[2][2])(lsolv[0])
# print(A1)
# opr = A1[0][0] * A1[1][1] * A1[2][2]\
#       + A1[0][1] * A1[1][2] * A1[2][0]\
#       + A1[0][2] * A1[1][0] * A1[2][1]\
#       - A1[0][2] * A1[1][1] * A1[2][0]\
#       - A1[0][1] * A1[1][0] * A1[2][2]\
#       - A1[0][0] * A1[1][2] * A1[2][1]
#
# x1 = A1[1][1] * A1[2][2] - A1[2][1] * A1[1][2]
# x2 = A1[1][2] * A1[2][0] - A1[2][2] * A1[1][0]
# x3 = A1[1][0] * A1[2][1] - A1[2][0] * A1[1][1]
#
# xx1 = [x1, x2, x3]
# print(xx1)
# max_x = max(xx1, key=abs)
# xx1 = [i/max_x for i in xx1]
# print()
# print("при l1:")
# print('X = (', *[str(myround(i)) + ',' for i in xx1], ')')
# print()
#
# A1 = copy.deepcopy(A)
# A1[0][0] = lambdify(l, A1[0][0])(lsolv[1])
# A1[1][1] = lambdify(l, A1[1][1])(lsolv[1])
# A1[2][2] = lambdify(l, A1[2][2])(lsolv[1])
# print(A1)
#
# opr = A1[0][0] * A1[1][1] * A1[2][2]\
#       + A1[0][1] * A1[1][2] * A1[2][0]\
#       + A1[0][2] * A1[1][0] * A1[2][1]\
#       - A1[0][2] * A1[1][1] * A1[2][0]\
#       - A1[0][1] * A1[1][0] * A1[2][2]\
#       - A1[0][0] * A1[1][2] * A1[2][1]
#
# x1 = A1[1][1] * A1[2][2] - A1[2][1] * A1[1][2]
# x2 = A1[1][2] * A1[2][0] - A1[2][2] * A1[1][0]
# x3 = A1[1][0] * A1[2][1] - A1[2][0] * A1[1][1]
# xx2 = [x1, x2, x3]
# print(xx2)
# max_x = max(xx2, key=abs)
# xx2 = [i/max_x for i in xx2]
# print("при l2:")
# print('X = (' ,*[str(myround(i)) + ',' for i in xx2],')')
#
#
#
# print()
# A1 = copy.deepcopy(A)
# A1[0][0] = lambdify(l, A1[0][0])(lsolv[2])
# A1[1][1] = lambdify(l, A1[1][1])(lsolv[2])
# A1[2][2] = lambdify(l, A1[2][2])(lsolv[2])
# print(A1)
#
# opr = A1[0][0] * A1[1][1] * A1[2][2]\
#       + A1[0][1] * A1[1][2] * A1[2][0]\
#       + A1[0][2] * A1[1][0] * A1[2][1]\
#       - A1[0][2] * A1[1][1] * A1[2][0]\
#       - A1[0][1] * A1[1][0] * A1[2][2]\
#       - A1[0][0] * A1[1][2] * A1[2][1]
# x1 = A1[1][1] * A1[2][2] - A1[2][1] * A1[1][2]
# x2 = A1[1][2] * A1[2][0] - A1[2][2] * A1[1][0]
# x3 = A1[1][0] * A1[2][1] - A1[2][0] * A1[1][1]
# xx3 = [x1, x2, x3]
# print(xx3)
# max_x = max(xx3, key=abs)
# xx3 = [i/max_x for i in xx3]
# print("при l3:")
# print('X = (' ,*[str(myround(i)) + ',' for i in xx3],')')


import copy

import numpy
from scipy.linalg import solve
from sympy import symbols, diff, lambdify, simplify, solve, expand

l, x = symbols('l, x')

def myround(num):
    return round(num, 5)



A = [
    [-4-l, 1, -1],
    [2, -2-l, 3],
    [3, 1, 3-l]
]


opr = A[0][0] * A[1][1] * A[2][2]\
      + A[0][1] * A[1][2] * A[2][0]\
      + A[0][2] * A[1][0] * A[2][1]\
      - A[0][2] * A[1][1] * A[2][0]\
      - A[0][1] * A[1][0] * A[2][2]\
      - A[0][0] * A[1][2] * A[2][1]

opr *= -1
print(opr)
opr = simplify(opr)
print(opr)
print()

df = diff(opr, l)
print("f'(l) = ", df)

solv = solve(df)
print(f"l1 = {myround(solv[0])}\n"
      f"l2 = {myround(solv[1])}")
# print(float(solv[0]), float(solv[1]))

f = lambdify(l, opr)

f1 = lambdify(l, df)

l0 = 0
l1 = l0 - f(l0)/ f1(l0)

print("Итерации:")
print("l0 = ", myround(l0))
print(f(l0), f1(l0), f(l0)/ f1(l0))
print("l1 = " ,myround(l1))
c = 2
while abs(l1 - l0) > 0.0001:
    l0 = l1
    print(f(l0), f1(l0), f(l0) / f1(l0))
    l1 = l0 - f(l0) / f1(l0)
    print(f"l{c} = ", myround(l1))
    c+= 1
print()
fl = expand(opr / (l-float(l0)))

lsolv = [complex(i).real for i in solve(fl)]
print(f"l1 = {myround(lsolv[0])}\n"
      f"l2 = {myround(lsolv[1])}\n"
      f"l3 = {myround(lsolv[2])}")


A1 = copy.deepcopy(A)
A1[0][0] = lambdify(l, A1[0][0])(lsolv[0])
A1[1][1] = lambdify(l, A1[1][1])(lsolv[0])
A1[2][2] = lambdify(l, A1[2][2])(lsolv[0])
print(A1)
opr = A1[0][0] * A1[1][1] * A1[2][2]\
      + A1[0][1] * A1[1][2] * A1[2][0]\
      + A1[0][2] * A1[1][0] * A1[2][1]\
      - A1[0][2] * A1[1][1] * A1[2][0]\
      - A1[0][1] * A1[1][0] * A1[2][2]\
      - A1[0][0] * A1[1][2] * A1[2][1]

x1 = A1[1][1] * A1[2][2] - A1[2][1] * A1[1][2]
x2 = A1[1][2] * A1[2][0] - A1[2][2] * A1[1][0]
x3 = A1[1][0] * A1[2][1] - A1[2][0] * A1[1][1]

xx1 = [x1, x2, x3]
print(xx1)
max_x = max(xx1, key=abs)
xx1 = [i/max_x for i in xx1]
print()
print("при l1:")
print('X = (', *[str(myround(i)) + ',' for i in xx1], ')')
print()

A1 = copy.deepcopy(A)
A1[0][0] = lambdify(l, A1[0][0])(lsolv[1])
A1[1][1] = lambdify(l, A1[1][1])(lsolv[1])
A1[2][2] = lambdify(l, A1[2][2])(lsolv[1])
print(A1)

opr = A1[0][0] * A1[1][1] * A1[2][2]\
      + A1[0][1] * A1[1][2] * A1[2][0]\
      + A1[0][2] * A1[1][0] * A1[2][1]\
      - A1[0][2] * A1[1][1] * A1[2][0]\
      - A1[0][1] * A1[1][0] * A1[2][2]\
      - A1[0][0] * A1[1][2] * A1[2][1]

x1 = A1[1][1] * A1[2][2] - A1[2][1] * A1[1][2]
x2 = A1[1][2] * A1[2][0] - A1[2][2] * A1[1][0]
x3 = A1[1][0] * A1[2][1] - A1[2][0] * A1[1][1]
xx2 = [x1, x2, x3]
print(xx2)
max_x = max(xx2, key=abs)
xx2 = [i/max_x for i in xx2]
print("при l2:")
print('X = (' ,*[str(myround(i)) + ',' for i in xx2],')')



print()
A1 = copy.deepcopy(A)
A1[0][0] = lambdify(l, A1[0][0])(lsolv[2])
A1[1][1] = lambdify(l, A1[1][1])(lsolv[2])
A1[2][2] = lambdify(l, A1[2][2])(lsolv[2])
print(A1)

opr = A1[0][0] * A1[1][1] * A1[2][2]\
      + A1[0][1] * A1[1][2] * A1[2][0]\
      + A1[0][2] * A1[1][0] * A1[2][1]\
      - A1[0][2] * A1[1][1] * A1[2][0]\
      - A1[0][1] * A1[1][0] * A1[2][2]\
      - A1[0][0] * A1[1][2] * A1[2][1]
x1 = A1[1][1] * A1[2][2] - A1[2][1] * A1[1][2]
x2 = A1[1][2] * A1[2][0] - A1[2][2] * A1[1][0]
x3 = A1[1][0] * A1[2][1] - A1[2][0] * A1[1][1]
xx3 = [x1, x2, x3]
print(xx3)
max_x = max(xx3, key=abs)
xx3 = [i/max_x for i in xx3]
print("при l3:")
print('X = (' ,*[str(myround(i)) + ',' for i in xx3],')')