from manim import *

from utils import derivative, get_solutions

class Scene14(Scene):
  def construct(self):
    func = lambda x: x**2 - 2
    
    axes = self.draw_background(func)
    self.draw_and_hide_solutions(axes, func)
    self.run_newton(axes, func, 0.75)
  
  def draw_background(self, func):
    """
    Draw the equation and the graph
    Return axes
    """
    # equation = MathTex(r"x^5", r" - 6x^4 + 4x^3 + 5x^2 - 2x + 1 = 0")
    equation = Text("x^2 - 2 = 0")
    axes = Axes(x_axis_config={"include_numbers": False})
    VGroup(equation, axes).arrange(DOWN)
    graph = axes.plot(func, color=BLUE)
    self.add(equation)
    self.play(Create(axes), Create(graph))
    self.wait(1)
    return axes

  def draw_and_hide_solutions(self, axes, func):
    sols = get_solutions(func)[:3]
    points = [Dot(axes.coords_to_point(x, 0), color=RED) for x in sols]
    self.play(*[Create(point) for point in points])
    self.wait(0.5)
    self.remove(*points)
    self.wait(0.5)

  def run_newton(self, axes: Axes, func, x: float):
    # text = MathTex(f"x = {x}").move_to(LEFT*2 + UP)
    text = Text(f"x = {x}").move_to(LEFT*4 + UP)
    self.play(Create(text))
    self.wait(0.5)
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
      
      self.play(Create(x_point))
      self.play(Create(vertical_line))
      self.play(Create(graph_point))
      self.remove(vertical_line)
      self.remove(graph_point)
    
    # def improve(x: float, text: MathTex):
    def improve(x: float, text: Text):
      """
      Return new guess
      """
      for _ in range(4):
        OFFSET = 10
        left_point = Dot(axes.coords_to_point(x - OFFSET, func(x) - OFFSET * deriv(x)))
        right_point = Dot(axes.coords_to_point(x + OFFSET, func(x) + OFFSET * deriv(x)))
        tangent = Line(left_point, right_point)
        self.play(Create(tangent))

        # New guess
        x = x - func(x) / deriv(x)
        
        #   new_text = MathTex(f"x = {round(x, 3)}").move_to(LEFT*2 + UP)
        new_text = Text(f"x = {round(x, 6)}").move_to(LEFT*4 + UP)
        self.play(Transform(text, new_text))
        draw_guess(x)
        self.remove(tangent)
    
    draw_guess(x)
    improve(x, text)