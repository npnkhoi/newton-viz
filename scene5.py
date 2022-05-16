from manim import *

class Scene5(Scene):
  def construct(self):
    # analytical = MathTex("2x^2+4x-1")
    # numerical = MathTex("\Delta = 4^2+4\\times2 = 24")
    a = Text("Analytical fails")
    b = Text("Numerical?")
    VGroup(a, b).arrange(DOWN)
    self.play(Write(a))
    self.wait(1)
    self.play(Write(b))
    self.wait(1)