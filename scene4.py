from manim import *

class Scene4(Scene):
  def construct(self):
    equation = MathTex(r"x^5", r" - 6x^4 + 4x^3 + 5x^2 - 2x + 1 = 0")
    comment = Text("Degree > 4, no general formula")
    VGroup(equation, comment).arrange(DOWN)
    frame = SurroundingRectangle(equation[0])
    self.play(Write(equation))
    self.wait(1)
    self.play(Create(frame))
    self.play(Write(comment))
    self.wait(2)