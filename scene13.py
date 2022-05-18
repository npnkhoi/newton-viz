from manim import *

class Scene_13(Scene):
    def construct(self):
       
        text_sim = Text("Simplicity", font_size=30)
        text_sim.shift(UP*3)
        text_sim.shift(LEFT*3)

        text_form = Text("x_{n+1} = x_n - \\frac{f(x_n)}{f'(x_n)}", font_size=30)
        text_form.shift(LEFT*3)

        # simplicity = Group(text_sim, text_form)
        # simplicity.arrange(DOWN)
        # simplicity.shift(LEFT*3)
# --------------
        text_rapid = Text("Rapid convergence", font_size=30)
        text_rapid.shift(UP*3)
        text_rapid.shift(RIGHT*3)

        # rapid = Group(text_rapid)
        # rapid.arrange(DOWN)
        # rapid.shift(RIGHT*3)

        self.play(
            FadeIn(text_sim, shift=RIGHT),
            FadeIn(text_form, shift=RIGHT),
        )

        self.wait(1)

        self.play(
            FadeIn(text_rapid, shift=LEFT)
        )  

        self.func = lambda x: x*x/9 - 2
        self.deriv = lambda x: 2/9 * x
        # self.draw_function()
        func = FunctionGraph(self.func, color=RED)
        # axes = Axes(axis_config={"include_numbers": True})
        axes = Axes()
        guess = 2
        guess_point = Dot([guess, self.func(guess), 0])
        # guess_point.shift(RIGHT*3)
        # guess_point.scale(0.5)
        # self.play(Create(guess_point))

        EPS = 0.001
        while (abs(self.func(guess)) > EPS):
            guess, guess_point = self.improve_guess(guess, guess_point, func, axes)
            # guess_point.shift(RIGHT*3)
            # guess_point.scale(0.5)
        self.wait(2)
       
    
    def improve_guess(self, guess: float, guess_point: Dot, func, axes) -> float:
        offset = 5
        # guess_point = Dot([guess, self.func(guess), 0])
        # self.add(guess_point)

        left_point = Dot([guess - offset, self.func(guess) - offset * self.deriv(guess), 0])
        # left_point.shift(RIGHT*3)
        # left_point.scale(0.5)

        right_point = Dot([guess + offset, self.func(guess) + offset * self.deriv(guess), 0])
        # right_point.shift(RIGHT*3)
        # right_point.scale(0.5)

        tangent = Line(left_point, right_point)
        # tangent.shift(RIGHT*3)
        # tangent.scale(0.5)

        new_guess = guess - self.func(guess) / self.deriv(guess)

        new_intersect = Dot([new_guess, 0, 0])
        # new_intersect.shift(RIGHT*3)
        # new_intersect.scale(0.5)

        g = Group(left_point, right_point, tangent, new_intersect, func, axes)
        g.shift(RIGHT*3)
        g.scale(0.5)

        self.play(FadeIn(g))

        # g.scale(2)
        g.shift(LEFT*3)

        # self.play(Create(tangent))
        # self.play(Create(new_intersect))
        self.remove(tangent, guess_point);

        new_guess_point = Dot([new_guess, self.func(new_guess), 0])
        vertical_line = DashedLine(new_intersect, new_guess_point)
        # vertical_line.shift(RIGHT*3)
        # vertical_line.scale(0.5)

        # self.add(vertical_line)
        # self.play(Create(new_guess_point))
        self.remove(vertical_line, new_intersect)
        return new_guess, new_guess_point
    
    def draw_function(self):
        func = FunctionGraph(self.func, color=RED)
        # axes = Axes(axis_config={"include_numbers": True})
        axes = Axes()

        # g=Group(func, axes)
        # g.shift(RIGHT*3)
        # g.scale(0.5)
        # self.add(axes)
        # self.play(Create(func)) 
        # self.play(FadeIn(g)) 
        return func, axes
