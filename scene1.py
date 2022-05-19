from manim import *

class Scene1(Scene):
  def construct(self):
    title = Text("Newton's method for solving equations")
    members = Text("Group 2K1P - Khoi, Khoa, Phuc")
    VGroup(title, members).arrange(DOWN)
    self.play(Write(title))
    self.play(Write(members))
    self.wait(4)