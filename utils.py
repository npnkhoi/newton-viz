from sympy import Symbol, solve, N, diff
from sympy.utilities.lambdify import lambdify
from sympy.abc import x

def get_solutions(func):
  """Returns solutions of a function"""
  f = func(x)
  sols = [N(sol) for sol in solve(f)]
  return sols

def derivative(func):
  d = diff(func(x))
  return lambdify(x, d)