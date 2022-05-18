from manim import *

class Scene10(Scene):
  def construct(self):
    guess = Tex("$x_i$")
    improve = MathTex(r"x_i \rightarrow x_{i+1}=", r"x_i-\frac{f(x_i)}{f'(x_i)}")
    rect = SurroundingRectangle(improve[1])
    self.add(guess)
    self.wait(1)
    self.play(Transform(guess, improve))
    self.wait(1)
    self.play(Create(rect))
    self.wait(1)