import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            for i in range(v):
                self.contents.append(k)

        self.initial_contents = copy.copy(self.contents)

    def draw(self, ball_num):
        try:
            drawn = random.sample(self.contents, ball_num)
        except ValueError:
            drawn = copy.copy(self.contents)

        for item in drawn:
            self.contents.remove(item)

        if len(self.contents) == 0:
            self.contents = copy.copy(self.initial_contents)
        return drawn

    def reset(self):
        self.contents = copy.copy(self.initial_contents)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_count = 0
    for i in range(num_experiments):
        expected_balls_working_copy = copy.copy(expected_balls)
        hat.reset()
        returned_balls = hat.draw(num_balls_drawn)
        for ball_color, ball_count in expected_balls.items():
            for b in range(ball_count):
                if ball_color in returned_balls:
                    returned_balls.remove(ball_color)
                    expected_balls_working_copy[ball_color] -= 1

        if sum(v for v in expected_balls_working_copy.values()) == 0:
            expected_count += 1

    prob = expected_count / num_experiments

    return prob
