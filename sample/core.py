

from os import system

from graphics import graphics_controller
from input_application import input_controller



render = graphics_controller()
key_input = input_controller()


system('clear')
render.drawBanner()
print("")
render.drawMenu()

while True:
    key_value=input()

    if int(key_value) == 9:
        break

    key_input.getKey(int(key_value),render)

