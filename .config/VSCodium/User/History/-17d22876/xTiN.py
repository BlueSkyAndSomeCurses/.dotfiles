import main
from manim import *
import numpy as np


class parenteses(Scene):
    def construct(self):
        possible = main.parentheses(4)
        text = Text(possible[0], font_size=90)
        counter = 0
        catalans_num = Text(f"C_n = {counter}", font_size=80)
        self.add(Text("C = 4").move_to(np.array([0, 3, 0])))
        self.add(catalans_num.move_to(np.array([0, -3, 0])))
        self.add(text)
        self.play(Write(text))

        for i in possible:
            counter += 1
            self.play(
                VGroup(
                    Transform(text, Text(i, font_size=90)),
                    Transform(catalans_num, Text(f"C_n = {counter}", font_size=80)),
                )
            )
