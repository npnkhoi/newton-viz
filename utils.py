import os
import wave
from sympy import Symbol, solve, N, diff
from sympy.utilities.lambdify import lambdify
from sympy.abc import x

EXAMPLE_FUNCTION = lambda x: x**5 - 6*x**4 + 4*x**3 + 5*x**2 - 2*x + 1
INITIAL_GUESS = 0.75
OFFSET = 10

def get_solutions(func):
  """Returns solutions of a function"""
  f = func(x)
  sols = [N(sol) for sol in solve(f)]
  return sols

def derivative(func):
  d = diff(func(x))
  return lambdify(x, d)

def show_audio_files():
  for root, dirs, files in os.walk('.'):
    for file in files:
      filename = os.path.join(root, file)
      with wave.open(filename, 'r') as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        print(duration)

if __name__ == "__main__":
  show_audio_files()