import copy
import random

class Hat:
    def __init__(self, **color) -> None:
        self.color = color
        self.contents = [key for key, val in self.color.items() for num in range(val)]

    def draw(self, num_balls):
        if num_balls > len(self.contents):
            return self.contents

        draw_balls = []
        for num in range(num_balls):
            rand_idx = random.randrange(len(self.contents))
            draw_balls.append(self.contents.pop(rand_idx))
        return draw_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass