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
    num_succes = 0
    for num in num_experiments:
        draw_balls = hat.draw(num_balls_drawn)
        succes = True
        for ball in expected_balls:
            if draw_balls.count(ball) < expected_balls[ball]:
                succes = False
        if succes:
            num_succes += 1
    return num_succes/num_experiments