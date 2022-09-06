from manim import *

class Test(Scene):
    def construct(self):
        dot_1 = Dot([-2, -1, 0])
        dot_2 = Dot([2, 1, 0])
        line = Line(dot_1.get_center(), dot_2.get_center()).set_color(BLUE)
        self.add(line, dot_1, dot_2)