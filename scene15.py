from cmath import cos
from manim import *
import numpy as np

class Scene_15(Scene):
    def construct(self):

        text = Text("Pitfalls", font_size=50)
        self.add(text)

        self.play(
            Write(text),
        )

        self.wait(4)

        self.play(
            text.animate.shift(UP*3)
        )

        differentiable_text = Text("The function is not differentiable at the guess")
        differentiable_text.shift(UP*3)

        self.play(Transform(text, differentiable_text))

        # guess = Tex("$x_i$")
        # improve = MathTex(r"x_i \rightarrow x_{i+1}=x_i+\frac{f(x_i)}", r"{f'(x_i)}")
        guess = Text("x_i")
        improve = Text("x_i \rightarrow x_{i+1}=x_i+\\frac{f(x_i)}")
        # rect = SurroundingRectangle(improve[1]) # uncomment when render Tex
        rect = SurroundingRectangle(improve[0])
        self.add(guess)
        self.wait(0.5)
        self.play(Transform(guess, improve))
        self.wait(0.5)
        self.play(Create(rect))
        self.wait(6)
        self.remove(guess, improve, rect)
        # ==================

        # close_zero_text = MathTex(r"f'(x_n) \\approx 0")
        close_zero_text = Text("f'(x_n) \\approx 0")
        close_zero_text.shift(UP*3 + LEFT*3)

        self.play(Transform(text, close_zero_text))

        func = lambda x: 1/x + np.cos(x)
    
        axes, graph = self.draw_background_close_zero(func)
        self.run_newton_close_zero(axes, func, 3.2)
        self.remove(axes, graph)
        # ==================

        perpetuation_text = Text("Perpetuation")
        perpetuation_text.shift(UP*3 + LEFT*3)

        self.play(Transform(text, perpetuation_text))

        func = lambda x: x**3-2*x+2
    
        axes, graph = self.draw_background_perpetuation(func)
        self.run_newton_perpetuation(axes, func, 0)
        self.remove(axes, graph)


    def draw_background_close_zero(self, func):
        """
        Draw the equation and the graph
        Return axes
        """
        axes = Axes(x_range=(-10,10,0.15), x_axis_config={"include_numbers": False})
        graph = axes.plot(func, color=BLUE)
        self.play(Create(axes), Create(graph))
        self.wait(1)
        return axes, graph


    def run_newton_close_zero(self, axes: Axes, func, x: float):
        deriv = lambda x : -1/x**2 - np.sin(x)
        
        def draw_guess(x: float):
            """
            Return the text
            """
            x_point = Dot(axes.coords_to_point(x, 0))
            graph_point = Dot(axes.coords_to_point(x, func(x)))
            vertical_line = DashedLine(x_point, graph_point)
            
            self.play(Create(x_point))
            self.play(Create(vertical_line))
            self.play(Create(graph_point))
            self.remove(x_point, vertical_line)

            OFFSET = 20
            left_point = Dot(axes.coords_to_point(x - OFFSET, func(x) - OFFSET * deriv(x)))
            right_point = Dot(axes.coords_to_point(x + OFFSET, func(x) + OFFSET * deriv(x)))
            tangent = Line(left_point, right_point)
            self.play(Create(tangent))

            self.wait(5)
            self.remove(graph_point, tangent)
        
        draw_guess(x)

    def draw_background_perpetuation(self, func):
        """
        Draw the equation and the graph
        Return axes
        """
        axes = Axes(x_axis_config={"include_numbers": False})
        graph = axes.plot(func, color=BLUE)
        self.play(Create(axes), Create(graph))
        self.wait(1)
        return axes, graph

    def run_newton_perpetuation(self, axes: Axes, func, x: float):
        deriv = lambda x : 3*x**2-2
        
        def draw_guess(x: float):
            """
            Return the text
            """
            x_point = Dot(axes.coords_to_point(x, 0))
            graph_point = Dot(axes.coords_to_point(x, func(x)))
            vertical_line = DashedLine(x_point, graph_point, color=RED)
            
            self.play(Create(x_point))
            self.play(Create(vertical_line), run_time=0.2)
            self.play(Create(graph_point))
            self.remove(x_point, vertical_line)
        
        def improve(x: float):
            """
            Return new guess
            """
            OFFSET = 10
            left_point = Dot(axes.coords_to_point(x - OFFSET, func(x) - OFFSET * deriv(x)))
            right_point = Dot(axes.coords_to_point(x + OFFSET, func(x) + OFFSET * deriv(x)))
            tangent = Line(left_point, right_point)
            self.play(Create(tangent), run_time = 0.2)

            # New guess
            x = x - func(x) / deriv(x)
            
            draw_guess(x)
            self.remove(tangent)
            
            return x
        
        draw_guess(x)
        for _ in range(4):
            x = improve(x)


    


    

