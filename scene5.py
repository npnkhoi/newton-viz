from manim import *

class Scene5(Scene):
  def construct(self):
    a = Text("Analytical fails")
    b = Text("Numerical?")
    VGroup(a, b).arrange(DOWN)
    self.play(Write(a))
    self.wait(1)
    self.play(Write(b))
    self.wait(1)