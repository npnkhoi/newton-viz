from manim import *

class Scene3(Scene):
  def construct(self):
    equation = MathTex("2x^2+4x-1")
    delta = MathTex("\Delta = 4^2+4\\times2 = 24")
    solutions = MathTex("x = \\frac{-2\\pm\\sqrt{6}}{2}")
    VGroup(equation, delta, solutions).arrange(DOWN)
    self.play(Write(equation))
    self.wait(1)
    self.play(Write(delta))
    self.play(Write(solutions))
    self.wait(2)