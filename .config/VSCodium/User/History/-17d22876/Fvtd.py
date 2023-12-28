import main
from manim import *
import numpy as np


class parenteses(Scene):
    def construct(self):
        possible = main.parentheses(5)
        text = Text(possible[0], font_size=90)
        self.add(Text("n = 4", font_size=80).move_to(np.array([-3, 2, 0])))
        self.add(text)
        self.play(Write(text))

        for i in possible:
            self.play(Transform(text, Text(i, font_size=90)))
