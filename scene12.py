from manim import *

class Scene_12(Scene):
    def construct(self):
        # banner = ManimBanner()
        # title = Title(f"Newton-Raphson Method")
        # self.add(banner, title)

        text = Text("Newton-Raphson Method", font_size=50)
        self.add(text)

        newton_img= ImageMobject("assets/img/Newton.jpeg")
        raphson_img = ImageMobject("assets/img/Anonymous.jpeg")

        newton_img.height = 5
        raphson_img.height = 5

        newton_img.shift(LEFT*3)
        newton_img.shift(DOWN)
        raphson_img.shift(RIGHT*3)
        raphson_img.shift(DOWN)

        newton_img.add(Text("Isaac Newton \n .").scale(0.5).next_to(newton_img,UP))
        raphson_img.add(Text("                    Joseph Raphson \n (Sorry! We could not find his portrait)").scale(0.5).next_to(raphson_img,UP))

        # x= Group(newton_img,raphson_img)
        # x.arrange()
        # self.add(x)

        self.play(
            Write(text),
        )
        self.wait(0.5)

        self.play(
            text.animate.shift(UP*3)
        )
        self.wait(1)

        self.play(
            FadeIn(newton_img, shift=RIGHT),
        )
        self.wait(1)
        self.play(
            FadeIn(raphson_img, shift=LEFT)
        )
        self.wait(1)
