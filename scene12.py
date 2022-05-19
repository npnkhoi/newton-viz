from manim import *

class Scene_12(Scene):
    def construct(self):

        text = Text("Newton-Raphson Method", font_size=50)

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

        self.play(
            Write(text),
        )
        self.wait(1.5)

        self.play(
            text.animate.shift(UP*3)
        )
        self.wait(1)

        self.play(
            FadeIn(newton_img, shift=RIGHT),
            FadeIn(raphson_img, shift=LEFT)
        )
        self.wait(2.5)
