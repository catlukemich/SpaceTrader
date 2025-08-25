import pygame
from pygame.locals import *
from .mode import *
import globvars

class ShipyardMode(Mode):

    def enable(self):
        globvars.shipyard_menu.show()


    def disable(self):
        globvars.shipyard_menu.hide()
        
        
    def onEvent(self, event):
        if event.type == KEYDOWN and event.key == K_RETURN:
            setMode(globvars.fly_mode)
