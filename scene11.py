from manim import *

class Scene11(Scene):
  def construct(self):
    question = Text("Stopping criterion?")
    answer1 = Tex(r"1) $|x_i - x_{i+1}| < \epsilon$")
    answer2 = Tex(r"2) $|f(x_i)| < \epsilon$")
    VGroup(question, answer1, answer2).arrange(DOWN)
    self.play(Create(question))
    self.wait(12)
    self.play(Create(answer1))
    self.wait(4)
    self.play(Create(answer2))
    self.wait(5)
    