from oxygen_generator import *
from solar_panel import *
from potato_farm import *


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.step_size = 10

        self.health = 100
        self.food_level = 100
        self.oxygen_tank_level = 100
        self.oxygen_area = False
        self.inventory = {}

        self.sprite = turtle.Turtle()
        self.sprite.shape("images/player_left.gif")
        self.sprite.penup()
        self.sprite.speed(0)

    def update_stats(self, oxygen_generators):
        if self.health > 0 and self.food_level == 0 or self.health > 0 and self.oxygen_tank_level == 0:
            self.health -= 1

        if self.food_level > 0:
            self.food_level -= 1

        if self.oxygen_tank_level > 0 and self.oxygen_area is False:
            self.oxygen_tank_level -= 1
        elif self.oxygen_tank_level < 100:
            self.oxygen_tank_level += 1

        for oxygen_generator in oxygen_generators:
            if oxygen_generator.powered is True and\
                    math.sqrt(((oxygen_generator.x - self.x)**2 +
                               (oxygen_generator.y - self.y)**2)) <= 200:
                self.oxygen_area = True
                break
            else:
                self.oxygen_area = False

        if self.food_level > 100:
            self.food_level = 100

    def update_sprite(self):
        if self.sprite.xcor() > self.x:
            self.sprite.shape("images/player_left.gif")
        elif self.sprite.xcor() < self.x:
            self.sprite.shape("images/player_right.gif")

        if self.sprite.pos != (self.x, self.y):
            self.sprite.setpos(self.x, self.y)

    def move_up(self):
        self.y += self.step_size

    def move_down(self):
        self.y -= self.step_size

    def move_left(self):
        self.x -= self.step_size

    def move_right(self):
        self.x += self.step_size

    def add_to_inventory(self, item_type, amount):
        if item_type not in self.inventory.keys():
            self.inventory[item_type] = amount
        else:
            self.inventory[item_type] += amount

    def remove_from_inventory(self, item_type, amount):
        if item_type in self.inventory.keys():
            self.inventory[item_type] -= amount
            if self.inventory[item_type] <= 0:
                del self.inventory[item_type]

    def mine(self):
        self.add_to_inventory("metal", random.randint(1, 3))

    def create_oxygen_generator(self, oxygen_generators):
        if "metal" in self.inventory.keys() and self.inventory["metal"] >= 10:
            oxygen_generator = OxygenGenerator(self.x, self.y)
            oxygen_generators.append(oxygen_generator)
            self.remove_from_inventory("metal", 10)

    def create_solar_panel(self, solar_panels):
        if "metal" in self.inventory.keys() and self.inventory["metal"] >= 15:
            solar_panel = SolarPanel(self.x, self.y)
            solar_panels.append(solar_panel)
            self.remove_from_inventory("metal", 10)

    def create_potato_farm(self, potato_farms):
        if "potato" in self.inventory.keys() and self.inventory["potato"] >= 1:
            potato_farm = PotatoFarm(self.x, self.y)
            potato_farms.append(potato_farm)
            self.remove_from_inventory("potato", 1)

    def eat_potato(self):
        if "potato" in self.inventory.keys() and self.inventory["potato"] >= 1 and self.food_level < 100:
            self.food_level += random.randint(20, 30)

            self.remove_from_inventory("potato", 1)

    def harvest_potato_farm(self, potato_farms):
        for potato_farm in potato_farms:
            if potato_farm.stage == 1 and\
                    math.sqrt(((potato_farm.x - self.x) ** 2 + (potato_farm.y - self.y) ** 2)) <= 100:
                self.add_to_inventory("potato", random.randint(1, 3))
                potato_farm.stage = 0
                break
