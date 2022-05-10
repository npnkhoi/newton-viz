import sympy

x = sympy.Symbol('x')
func = x * x - 2

def newton(func, guess=0.1, eps=0.001):
  """Newton method to find root of func"""
  derivative = sympy.diff(func, sympy.Symbol('x'))

  while True:
    guess = guess - func.subs(x, guess) / derivative.subs(x, guess)
    print('new guess:', guess)
    if abs(func.subs(x, guess)) < eps:
      break
  
  return guess

newton(func)