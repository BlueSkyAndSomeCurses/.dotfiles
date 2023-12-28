import main
from manim import *
import numpy as np


class parenteses(Scene):
    def construct(self):
        possible = main.parentheses(4)
        text = Text(possible[0], font_size=90)
        counter = 0
        c_n = Tex(r"C_n =", font_size=80)
        cn_pos = np.array([-0.5, -3, 0])
        self.add(
            Text("C = 4", font_size=80, color="yellow").move_to(np.array([0, 3, 0]))
        )
        self.add(c_n.move_to(cn_pos))
        self.add(text)
        self.play(Write(text))

        for i in possible:
            counter += 1
            self.play(
                Transform(text, Text(i, font_size=90)),
                Transform(
                    catalans_num,
                    Tex(r"C_n = {counter}", font_size=80).move_to(catalans_pos),
                ),
                runtime=0.5,
            )

        self.wait(5)
