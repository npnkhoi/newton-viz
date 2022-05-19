from matplotlib.transforms import Transform
from manim import *

class Scene16(Scene):
    def construct(self):
        # banner = ManimBanner()
        # title = Title(f"Newton-Raphson Method")
        # self.add(banner, title)

        text1 = Text("Newton-Raphson Method", font_size=40)
        self.add(text1)   

        self.play(
            Write(text1),
        )
        self.wait(1)

        text11 = Text("is an incredibly powerful numerical method for finding roots", font_size=30, 
        t2c={"numerical":YELLOW, "roots": YELLOW})
        text11.shift(DOWN)
        self.play(FadeIn(text11, shift=DOWN))
        self.wait(4)
        self.play(FadeOut(text11, shift=DOWN))

        self.play(text1.animate.shift(UP))

        # self.play(
        #     text1.animate.shift(LEFT*3)
        # )

        text2 = Text("Secant Method", font_size=40)
        self.add(text2)
        self.play(FadeIn(text2, shift=LEFT))

        text3 = Text("Bisection Method", font_size=40)
        text3.shift(DOWN)
        self.add(text3)
        self.play(FadeIn(text3, shift=RIGHT))

        self.wait(1.5)

        self.play(FadeOut(text2, shift=RIGHT))
        self.play(FadeOut(text3, shift=LEFT))

        text4 = Text(
            """
            Newton-Raphson Method is simple and fast. 
            """,
            font_size=40,
            # t2c is a dict that you can choose color for different text
            t2c={"simple": BLUE, "fast": YELLOW}
        )
        self.wait(1)
        self.play(Transform(text1, text4))
        self.wait(3)
        self.play(Transform(text1, Text("The End", font_size=60)))



