import main
from manim import *


class parenteses(Scene):
    def construct(self):
        possible = main.parentheses(4)
        text = Text(possible[0], font_size=90)
        self.add(Text("n = 4"))
        self.play(Write(text))
        self.add(text)

        for i in possible:
            self.play(Transform(text, Text(i, font_size=90)))
