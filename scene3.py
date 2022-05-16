from manim import *

class Scene3(Scene):
  def construct(self):
    # equation = MathTex(r"\log_2{x}^2 - 3\log_2{x} + 2 = 0")
    equation = MathTex(r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots")
    subs = MathTex("\\text{Let } t = \\log_2{x}")
    easy = MathTex("t^2 + 3t - 2 = 0 \\text{ (easy)}")
    VGroup(equation, subs, easy).arrange(DOWN)
    self.play(Write(equation))
    self.wait(1)
    self.play(Write(subs))
    self.wait(1)
    self.play(Write(easy))
    self.wait(2)