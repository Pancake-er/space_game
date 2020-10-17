from player import *
import turtle

window = turtle.Screen()
window.bgcolor("light salmon")

window.register_shape("images/player_left.gif")
window.register_shape("images/player_right.gif")
window.register_shape("images/solar_panel.gif")
window.register_shape("images/oxygen_generator_on.gif")
window.register_shape("images/oxygen_generator_off.gif")
window.register_shape("images/potato_farm_young.gif")
window.register_shape("images/potato_farm_grown.gif")
window.register_shape("images/potato_farm_cold.gif")

main_update_speed = 1000
sprite_update_speed = 10

text = turtle.Turtle()
text.ht()
text.up()
text.speed(0)
text.setpos(-600, 500)
text.setpos(-600, 500)

player = Player(0, 0)
player.inventory["potato"] = 1

oxygen_generators = []
solar_panels = []
potato_farms = []


def main_update():
    player.update_stats(oxygen_generators)

    for oxygen_generator in oxygen_generators:
        oxygen_generator.update_stats(solar_panels)

    for potato_farm in potato_farms:
        potato_farm.update_stats(oxygen_generators)

    text.undo()
    text.write("Health: %s | Food Level: %s | Oxygen Tank Level: %s | Inventory: %s" % (player.health,
                                                                                        player.food_level,
                                                                                        player.oxygen_tank_level,
                                                                                        str(player.inventory)),
               font=("Arial", 16, "normal"))

    turtle.ontimer(main_update, main_update_speed)


def sprite_update():
    player.update_sprite()

    for oxygen_generator in oxygen_generators:
        oxygen_generator.update_sprite()

    for potato_farm in potato_farms:
        potato_farm.update_sprite()
    turtle.ontimer(sprite_update, sprite_update_speed)


def create_oxygen_generator():
    player.create_oxygen_generator(oxygen_generators)


def create_solar_panel():
    player.create_solar_panel(solar_panels)


def create_potato_farm():
    player.create_potato_farm(potato_farms)


def harvest_potato_farm():
    player.harvest_potato_farm(potato_farms)


main_update()
sprite_update()

turtle.listen()
turtle.onkeypress(player.move_up, "w")
turtle.onkeypress(player.move_down, "s")
turtle.onkeypress(player.move_left, "a")
turtle.onkeypress(player.move_right, "d")
turtle.onkey(player.mine, "1")
turtle.onkey(create_solar_panel, "2")
turtle.onkey(create_oxygen_generator, "3")
turtle.onkey(create_potato_farm, "4")
turtle.onkey(player.eat_potato, "q")
turtle.onkey(harvest_potato_farm, "e")

turtle.mainloop()
