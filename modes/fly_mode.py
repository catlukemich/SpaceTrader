from pygame.mixer import Sound
from gui.fly_hud import FlyHud
from modes.mode import *
from pygame.locals import *
import globvars
import pygame
from mathutils import *
from main      import *
from gui.fly_hud import *

ENTERING_PROXIMITY = 40 # The distance below which an object can be entered

class FlyMode(Mode):

    def __init__(self):
        self.fly_hud = FlyHud()
        self.tab_pressed = False

    def onEvent(self, event):
        player = globvars.player
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                player.setRotatingLeft(True)
            if event.key == K_RIGHT:
                player.setRotatingRight(True)
            if event.key == K_UP:
                player.setAccelerating(True)
            if event.key == K_DOWN:
                player.setDecelerating(True)
            if event.key == K_d:
                if self.nearby_dock != None:
                    globvars.player.setSpeed(0)
                    globvars.player.rotating_left = False
                    globvars.player.rotating_right = False
                    globvars.dock = self.nearby_dock
                    setMode(globvars.dock_mode)
            if event.key == K_TAB:  # Tab key to view the carried cargos.
                self.tab_pressed = True
                self.displayCargo()
            if event.key == K_RETURN: # Enter for entering the shipyard.
                if self.nearby_shipyard != None:
                    setMode(globvars.shipyard_mode)

            if event.key == K_LCTRL or event.key == K_RCTRL:
                player.shoot()

        elif event.type == KEYUP:
            if event.key == K_LEFT:
                player.setRotatingLeft(False)
            if event.key == K_RIGHT:
                player.setRotatingRight(False)
            if event.key == K_UP:
                player.setAccelerating(False)
            if event.key == K_DOWN:
                player.setDecelerating(False)

            if event.key == K_TAB:
                self.tab_pressed = False
                self.hideCargo()
        else:
            if not self.tab_pressed:
                self.fly_hud.onEvent(event)

    def displayCargo(self):
        globvars.cargo_panel.show()

    def hideCargo(self):
        globvars.cargo_panel.hide()

    def update(self):
        globvars.viewport.center.x = globvars.player.position.x
        globvars.viewport.center.y = globvars.player.position.y

        # Nearby dock contact detection:
        self.nearby_dock = None
        for dock in globvars.docks:
            if dock.position.distance(globvars.player.position) < ENTERING_PROXIMITY:
                self.nearby_dock = dock
                break

        # Nearby shipyard contact detection:
        self.nearby_shipyard = None
        for shipyard in globvars.shipyards:
            if shipyard.position.distance(globvars.player.position) < ENTERING_PROXIMITY:
                self.nearby_shipyard = shipyard
                break

        # Asteroid collision detection:
        for asteroid in globvars.asteroids:
            if asteroid.position.distance(globvars.player.position) < 50:
                collision_sound = Sound("assets/sounds/collision.ogg")
                collision_sound.play()
                globvars.player.setSpeed(2)

        if self.tab_pressed:
            globvars.cargo_panel.update()

        self.fly_hud.update()

    def draw(self):
        self.fly_hud.draw(self.nearby_dock, self.nearby_shipyard)
