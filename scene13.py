from manim import *

class Scene_13(Scene):
    def construct(self):
       
        # text_form = MathTex(r"x_{n+1} = x_n - ",r"\frac{f(x_n)}{f'(x_n)}", font_size=30)
        text_form = Text("x_{n+1} = x_n - \\frac{f(x_n)}{f'(x_n)}", font_size=30)
        self.play(FadeIn(text_form, shift=DOWN))
        self.wait(3)

        text_sim = Text("Simplicity", font_size=40, color=BLUE)
        text_sim.shift(UP*2)
        text_sim.shift(LEFT*3)
        self.play(FadeIn(text_sim, shift=RIGHT))
        self.wait(2)
        # rect = SurroundingRectangle(text_form[1]) # uncomment when render Tex
        rect = SurroundingRectangle(text_form[0])
        self.play(Create(rect))
        self.wait(2)

        text_rapid = Text("Rapid convergence", font_size=40, color=YELLOW)
        text_rapid.shift(UP*2)
        text_rapid.shift(RIGHT*3)
        self.play(FadeIn(text_rapid, shift=LEFT))
        self.wait(5)

        
