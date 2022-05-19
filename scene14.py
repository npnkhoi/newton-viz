from manim import *

from utils import derivative, get_solutions

class Scene14(Scene):
  def construct(self):
    
    text = Tex("Approximation of irrational number", font_size=50)
    self.play(Write(text))
    self.wait(5)
    self.play(FadeOut(text))

    text_sqrt = MathTex("\sqrt{2} = ?", font_size=50)
    # text_sqrt = Tex("sqrt 2 = ?", font_size=50)
    self.play(Write(text_sqrt))
    self.wait(2)
    self.play(FadeOut(text_sqrt))

    func = lambda x: x**2 - 2
    
    axes = self.draw_background(func)
    self.run_newton(axes, func, 0.75)
  
  def draw_background(self, func):
    """
    Draw the equation and the graph
    Return axes
    """
    equation = MathTex(r"x^2 - 2 = 0")
    # equation = Tex("x^2 - 2 = 0")
    axes = Axes(x_axis_config={"include_numbers": False})
    VGroup(equation, axes).arrange(DOWN)
    graph = axes.plot(func, color=BLUE)
    self.add(equation)
    self.play(Create(axes), Create(graph))
    return axes

  def run_newton(self, axes: Axes, func, x: float):
    text = MathTex(f"x = {x}").move_to(LEFT*4 + UP)
    # text = Tex(f"x = {x}").move_to(LEFT*4 + UP)
    self.play(Create(text))
    deriv = derivative(func)
    
    def draw_guess(x: float):
      """
      Return the text
      """
      x_point = Dot(axes.coords_to_point(x, 0), color=RED)
      graph_point = Dot(axes.coords_to_point(x, func(x)), color=RED)
      x_point.scale(0.5)
      graph_point.scale(0.5)
      vertical_line = DashedLine(x_point, graph_point)
      
      self.play(Create(x_point), run_time=0.5)
      self.play(Create(vertical_line), run_time=0.5)
      self.play(Create(graph_point), run_time=0.5)
      self.remove(vertical_line)
      self.remove(graph_point)
    
    def improve(x: float, text: MathTex):
    # def improve(x: float, text: Text):
      """
      Return new guess
      """
      for _ in range(4):
        OFFSET = 10
        left_point = Dot(axes.coords_to_point(x - OFFSET, func(x) - OFFSET * deriv(x)))
        right_point = Dot(axes.coords_to_point(x + OFFSET, func(x) + OFFSET * deriv(x)))
        tangent = Line(left_point, right_point)
        self.play(Create(tangent), run_time = 0.2)

        x = x - func(x) / deriv(x)
        
        new_text = MathTex(f"x = {round(x, 6)}").move_to(LEFT*4 + UP)
        # new_text = Tex(f"x = {round(x, 6)}").move_to(LEFT*4 + UP)
        self.play(Transform(text, new_text))
        draw_guess(x)
        self.remove(tangent)
    
    draw_guess(x)
    improve(x, text)