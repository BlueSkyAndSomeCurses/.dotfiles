import main
from manim import *


class parenteses(Scene):
    def construct(self):
        possible = main.parentheses(4)
        text = Text(possible[0], font_size=90)
        self.add(
            VGroup(Text("n = 4", font_size=80, color="yellow"), text).arrange(DOWN)
        )
        self.play(Write(text))

        for i in possible:
            self.play(Transform(text, Text(i, font_size=90)))
