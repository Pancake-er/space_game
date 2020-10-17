import turtle


class SolarPanel:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.sprite = turtle.Turtle()
        self.sprite.shape("images/solar_panel.gif")
        self.sprite.penup()
        self.sprite.speed(0)
        self.sprite.setpos(self.x, self.y)
