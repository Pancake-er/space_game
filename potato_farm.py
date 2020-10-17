import turtle
import math
import random


class PotatoFarm:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.oxygen_area = False
        self.stage = 0

        self.sprite = turtle.Turtle()
        self.sprite.shape("images/potato_farm_cold.gif")
        self.sprite.penup()
        self.sprite.speed(0)
        self.sprite.setpos(self.x, self.y)

    def update_stats(self, oxygen_generators):
        for oxygen_generator in oxygen_generators:
            if oxygen_generator.powered is True and math.sqrt(
                    ((oxygen_generator.x - self.x) ** 2 +
                     (oxygen_generator.y - self.y) ** 2)) <= 100:
                self.oxygen_area = True
                break
            else:
                self.oxygen_area = False

        if self.stage == 0 and self.oxygen_area is True and random.randint(1, 35) == 1:
            self.stage = 1

    def update_sprite(self):
        if self.stage == 1:
            self.sprite.shape("images/potato_farm_grown.gif")
        elif self.stage == 0 and self.oxygen_area is True:
            self.sprite.shape("images/potato_farm_young.gif")
