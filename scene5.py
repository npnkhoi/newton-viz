from manim import *

class Scene5(Scene):
  def construct(self):
    a = Tex("Analytical fails")
    b = Tex("Numerical?")
    VGroup(a, b).arrange(DOWN)
    self.play(Write(a))
    self.wait(6)
    self.play(Write(b))
    self.wait(3)