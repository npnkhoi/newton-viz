from manim import *

class Scene3(Scene):
  def construct(self):
    equation = MathTex(r"\log_2{x}^2 - 3\log_2{x} + 2 = 0 \text{ (1)}")
    subs = MathTex(r"\text{Let } t = \log_2{x}")
    easy = MathTex(r"(1) \Leftrightarrow t^2 + 3t - 2 = 0 \text{ (easy)}")
    VGroup(equation, subs, easy).arrange(DOWN)
    self.play(Write(equation))
    self.wait(1)
    self.play(Write(subs))
    self.wait(1)
    self.play(Write(easy))
    self.wait(2)