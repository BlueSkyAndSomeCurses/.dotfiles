import main
from manim import *
import numpy as np


class parenteses(Scene):
    def construct(self):
        possible = main.parentheses(6)
        text = Text(possible[0], font_size=90)

        counter = 0
        cn_pos = np.array([0, -3, 0])
        catalans = Text(f"C_n = {counter}", font_size=80)

        self.add(
            Text("C = 6", font_size=80, color="yellow").move_to(np.array([0, 3, 0]))
        )

        self.add(catalans.move_to(cn_pos), text)

        # self.add(text)

        self.play(Write(text))

        for i in possible:
            counter += 1
            self.play(
                Transform(text, Text(i, font_size=90)),
                Transform(
                    catalans,
                    Text(f"C_n = {counter}", font_size=80).move_to(cn_pos),
                ),
                runtime=0.5,
            )

        self.wait(5)
