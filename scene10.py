from manim import *

from utils import EXAMPLE_FUNCTION, INITIAL_GUESS, OFFSET, derivative

class Scene10(Scene):
  def construct(self):
    # "The intuition is just that!"
    func = EXAMPLE_FUNCTION
    axes = Axes(x_axis_config={"include_numbers": True}).scale(0.5).to_edge(LEFT)
    graph = axes.plot(func, color=BLUE)
    self.add(axes, graph)

    intuit = Tex("Intuitive").next_to(axes, RIGHT)
    formal = Tex(r"$\rightarrow$ Formal") \
      .next_to(intuit, RIGHT)
    self.play(Write(intuit))
    self.wait(5)
    self.play(Write(formal))
    self.wait(3)
    self.play(FadeOut(intuit), FadeOut(formal))

    # Guess x_i
    x = INITIAL_GUESS
    guess_point = Dot(axes.coords_to_point(x, 0))
    guess_text = MathTex(r"x_i = \text{anything}")
    tangent_function = MathTex("f(x) = f'(x)(x - x_i) + f(x_i)")
    newton_formula = MathTex(r"x_{i+1}=x_i-\frac{f(x_i)}{f'(x_i)}")
    VGroup(guess_text, tangent_function, newton_formula) \
      .arrange(DOWN).next_to(axes, RIGHT)
    tangent_equation = MathTex("f'(x)(x - x_i) + f(x_i) = 0") \
      .align_to(tangent_function, LEFT).align_to(tangent_function, UP)

    self.play(Create(guess_point), Write(guess_text))
    self.wait(3)

    # tangent line
    graph_point = Dot(axes.coords_to_point(x, func(x)))
    vertical = DashedLine(guess_point, graph_point)
    self.play(Create(graph_point), Create(vertical))
    
    deriv = derivative(func)
    left_point = Dot(axes.coords_to_point(x - OFFSET, func(x) - OFFSET * deriv(x)))
    right_point = Dot(axes.coords_to_point(x + OFFSET, func(x) + OFFSET * deriv(x)))
    tangent = Line(left_point, right_point)
    self.play(Create(tangent))
    self.play(Write(tangent_function))
    self.wait(6)
    self.play(Transform(tangent_function, tangent_equation))
    self.wait(6)
    self.play(Write(newton_formula))
    
    rect = SurroundingRectangle(newton_formula)
    self.wait(2)
    self.play(Create(rect))
    self.wait(7)



  # def construct(self):
  #   question = Tex("Formal method?")
  #   guess = Tex("$x_i$")
  #   improve = MathTex(r"x_i \rightarrow x_{i+1}=", r"x_i-\frac{f(x_i)}{f'(x_i)}")
  #   rect = SurroundingRectangle(improve[1])
  #   self.add(question)
  #   self.wait(3)
  #   self.play(Transform(question, guess))
  #   self.wait(30)
  #   self.remove(question)
  #   self.play(Transform(guess, improve))
  #   self.wait(1)
  #   self.play(Create(rect))
  #   self.wait(1)
