import main
from manim import *
import numpy as np


class parenteses(Scene):
    def construct(self):
        possible = main.parentheses(4)
        text = Text(possible[0], font_size=90)
        counter = 0
        self.add(
            Text("n = 4", font_size=80, color="yellow").move_to(np.array([0, 3, 0]))
        )
        self.add(text)
        self.play(Write(text))

        for i in possible:
            self.play(Transform(text, Text(i, font_size=90)))
