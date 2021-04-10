
import downloaderops
from graphics import graphics_controller

from os import system

class input_controller:
    def __init__(self):
        pass

    def getKey(self,value,screen):

        try:
            if value <= 0 or value > 9:
                print("Choose a value between 1 and 7")
            else:
                if value==1:
                   downloaderops.deploy()
                   system('clear')
                   screen.reloadRender()
        except:
            print("an Exception occurred")
