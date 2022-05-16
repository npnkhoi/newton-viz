"""
BUG: mismatch between the axes and the real value
"""

from manim import *


class Newton(MovingCameraScene):
    def construct(self):
        self.func = lambda x: x*x/9 - 2
        self.deriv = lambda x: 2/9 * x
        self.draw_function()

        guess = 2
        guess_point = Dot([guess, self.func(guess), 0])
        text = MathTex(f"x = {guess}").move_to((RIGHT + UP) * 2)
        self.play(Create(guess_point))
        # self.focus_on_point(guess_point)
        self.add(text)

        EPS = 0.001
        while (abs(self.func(guess)) > EPS):
            guess, guess_point, text = self.improve_guess(guess, guess_point, text)
        self.wait(2)
    
    def improve_guess(self, guess: float, guess_point: Dot, text: MathTex) -> float:
        offset = 10
        left_point = Dot([guess - offset, self.func(guess) - offset * self.deriv(guess), 0])
        right_point = Dot([guess + offset, self.func(guess) + offset * self.deriv(guess), 0])
        
        tangent = Line(left_point, right_point)
        new_guess = guess - self.func(guess) / self.deriv(guess)
        new_intersect = Dot([new_guess, 0, 0])
        self.play(Create(tangent))
        self.play(Create(new_intersect))
        self.focus_on_point(new_intersect)
        self.remove(tangent, guess_point);

        new_guess_point = Dot([new_guess, self.func(new_guess), 0])
        vertical_line = DashedLine(new_intersect, new_guess_point)
        self.add(vertical_line)
        self.play(Create(new_guess_point))
        self.remove(text)
        text = MathTex(f'x = {round(new_guess, 5)}').move_to((RIGHT + UP) * 2)
        self.add(text)
        self.focus_on_point(new_guess_point, new_height=5 * abs(new_guess_point.get_y()))
        self.remove(vertical_line, new_intersect)
        return new_guess, new_guess_point, text
    
    def draw_function(self):
        func = FunctionGraph(self.func, color=RED)
        axes = Axes(axis_config={"include_numbers": True})
        self.add(axes)
        self.play(Create(func))
    
    def focus_on_point(self, p: Dot, new_height=None):
        return
        self.play(self.camera.frame.animate.move_to(p))
        # if new_height is not None:
        #     self.play(self.camera.frame.animate.set(height=new_height))
