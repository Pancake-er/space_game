import turtle
import math


class OxygenGenerator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.powered = False

        self.sprite = turtle.Turtle()
        self.sprite.shape("images/oxygen_generator_off.gif")
        self.sprite.penup()
        self.sprite.speed(0)
        self.sprite.setpos(self.x, self.y)

    def update_stats(self, solar_panels):
        for solar_panel in solar_panels:
            if math.sqrt(((solar_panel.x - self.x)**2 + (solar_panel.y - self.y)**2)) <= 200:
                self.powered = True
                break
            else:
                self.powered = False

    def update_sprite(self):
        if self.sprite.shape() == "images/oxygen_generator_off.gif" and self.powered is True:
            self.sprite.shape("images/oxygen_generator_on.gif")
