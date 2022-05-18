from manim import *

class Scene_16(Scene):
    def construct(self):
        # banner = ManimBanner()
        # title = Title(f"Newton-Raphson Method")
        # self.add(banner, title)

        text = Text("Pitfalls", font_size=50)
        self.add(text)

        self.play(
            Write(text),
        )
        self.wait(0.5)

        self.play(
            text.animate.shift(UP*3)
        )

