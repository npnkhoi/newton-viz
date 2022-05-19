from manim import *

class Scene15_2(Scene):
    def construct(self):

        text = Text("Perpetuation", font_size=50)
        text.shift(UP*3 + LEFT*3)
        self.add(text)
        # ==================

        unwanted_text = Text("Unwanted root")
        unwanted_text.shift(UP*3 + LEFT*3)

        self.play(Transform(text, unwanted_text))

        func = lambda x: x**3 + 3*x**2 -x-3    
        axes, graph = self.draw_background_unwanted(func)
        self.draw_wanted_solutions(axes, func)
        self.run_newton_unwanted(axes, func, 0)
        self.remove(axes, graph)

    def draw_background_unwanted(self, func):
        """
        Draw the equation and the graph
        Return axes
        """
        axes = Axes(x_axis_config={"include_numbers": False})
        graph = axes.plot(func, color=BLUE)
        self.play(Create(axes), Create(graph))
        return axes, graph

    def draw_wanted_solutions(self, axes, func):
        point = Dot(axes.coords_to_point(-1, 0), color=RED)
        self.play(Create(point))
        rect = SurroundingRectangle(point)
        self.play(Create(rect))

    def run_newton_unwanted(self, axes: Axes, func, x: float):
        deriv = lambda x : 3*x**2 + 6*x - 1
        
        def draw_guess(x: float):
            """
            Return the text
            """
            x_point = Dot(axes.coords_to_point(x, 0))
            graph_point = Dot(axes.coords_to_point(x, func(x)))
            vertical_line = DashedLine(x_point, graph_point, color=RED)
            
            self.play(Create(x_point))
            self.play(Create(vertical_line))
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
            self.play(Create(tangent))

            # New guess
            x = x - func(x) / deriv(x)
            
            draw_guess(x)
            self.remove(tangent)
            
            return x
        
        draw_guess(x)
        for _ in range(1):
            x = improve(x)


    


    

