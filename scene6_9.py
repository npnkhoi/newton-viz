from manim import *

from utils import EXAMPLE_FUNCTION, OFFSET, derivative, get_solutions

class Scene6_9(Scene):
  def construct(self):
    func = EXAMPLE_FUNCTION
    
    axes = self.draw_background(func)
    self.wait(16.5)
    self.draw_and_hide_solutions(axes, func)
    self.run_newton(axes, func, 0.75)
  
  def draw_background(self, func):
    """
    Draw the equation and the graph
    Return axes
    """
    equation = MathTex(r"x^5", r" - 6x^4 + 4x^3 + 5x^2 - 2x + 1 = 0")
    axes = Axes(x_axis_config={"include_numbers": True})
    VGroup(equation, axes).arrange(DOWN)
    graph = axes.plot(func, color=BLUE)
    self.add(equation)
    self.play(Create(axes), Create(graph))
    self.wait(1)
    return axes

  def draw_and_hide_solutions(self, axes, func):
    sols = get_solutions(func)[:3]
    points = [Dot(axes.coords_to_point(x, 0), color=RED) for x in sols]
    for point in points:
      self.play(Create(point))
    self.wait(4)
    self.remove(*points)
    self.wait(1)

  def run_newton(self, axes: Axes, func, x: float):
    text = MathTex(f"x = {x}").move_to(LEFT*2 + UP)
    self.play(Create(text))
    deriv = derivative(func)
    
    def draw_guess(x: float, slow=False):
      """
      Return the text
      """
      x_point = Dot(axes.coords_to_point(x, 0))
      graph_point = Dot(axes.coords_to_point(x, func(x)))
      vertical_line = DashedLine(x_point, graph_point)
      
      self.play(Create(x_point))
      if slow:
        self.wait(1)
      self.play(Create(vertical_line))
      self.play(Create(graph_point))
      self.remove(x_point, vertical_line)
    
    def improve(x: float, text: MathTex, slow=False):
      """
      Return new guess
      """
      left_point = Dot(axes.coords_to_point(x - OFFSET, func(x) - OFFSET * deriv(x)))
      right_point = Dot(axes.coords_to_point(x + OFFSET, func(x) + OFFSET * deriv(x)))
      tangent = Line(left_point, right_point)
      if slow:
        self.wait(2)
      self.play(Create(tangent))
      if slow:
        self.wait(6)

      # New guess
      x = x - func(x) / deriv(x)
      
      new_text = MathTex(f"x = {round(x, 6)}").move_to(LEFT*3 + UP)
      print(f'Transforming from {id(text)} to {id(new_text)}')
      
      # self.play(Transform(text, new_text))
      self.remove(text)
      self.add(new_text)
      print(f'Transformed from {id(text)} to {id(new_text)}')
      
      draw_guess(x)
      self.remove(tangent)
      
      return x, new_text
    
    draw_guess(x, slow=True)
    for i in range(5):
      x, text = improve(x, text, slow=(i==0))