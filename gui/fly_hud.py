import pygame
from pygame.locals import *
import globvars
from gui.hud_guide import HudGuide
from main      import *
from mathutils import Vector2, map_value


class FlyHud:

    def __init__(self):
        self.dock_guides = {} # A map from a docks instances to docks guides
        self.shipyard_guides = {} # A map from a shipyards instances to shipyards guides


    def update(self):
        self.dock_guides = {}
        for dock in globvars.docks:
            dock_guide = HudGuide(dock, 350, 0, 90000)
            self.dock_guides[dock] = dock_guide

        self.shipyard_guides = { }
        for shipyard in globvars.shipyards:
            shipyard_guide = HudGuide(shipyard, 350, 0, 90000)
            shipyard_guide.setColor((152, 48, 255))
            self.shipyard_guides[shipyard] = shipyard_guide

        globvars.cargo_panel.update()


    def draw(self, nearby_dock, nearby_shipyard):
        
        # Draw the navigation circle around the screen:
        pygame.draw.circle(globvars.surface, 
                           (200, 200, 200), 
                           (globvars.surface.get_width() / 2, globvars.surface.get_height() / 2), 
                           350, 2)

        # Draw all the guides - to docks, to shipyards and to asteroids #
        for dock in self.dock_guides:
            dock_guide = self.dock_guides[dock]
            if dock is not nearby_dock:
                dock_guide.draw()
            
        for shipyard in self.shipyard_guides:
            shipyard_guide = self.shipyard_guides[shipyard]
            if shipyard is not nearby_shipyard:
                shipyard_guide.draw()

        asteroids = globvars.asteroids
        for ast in asteroids:
            # Draw the guide of an asteroid:
            ast_guide = HudGuide(ast,200, 2000, 8000)
            ast_guide.setShowDistance(False).setColor((245, 194, 66))
            ast_guide.draw()

        # If dock or shipyard is locally present - show the player information how to enter them #
        font = pygame.font.Font("assets/gui/LCD14.ttf", 15)
        if nearby_dock != None:
            txt = font.render("Press \"D\" to enter " + nearby_dock.name + " spacedock.", 1, (255, 255, 255))
            globvars.surface.blit(txt, (220, 0))

        if nearby_shipyard != None:
            txt = font.render("Press \"ENTER\" to enter the shipyard.", 1, (255, 255, 255))
            globvars.surface.blit(txt, (220, 0))


    def onEvent(self, event):
        if event.type == MOUSEMOTION:
            globvars.cargo_panel.setDrawButtons(True)
            globvars.cargo_panel.hide()
            globvars.cargo_panel.setDock(None)

            x = event.pos[0]
            y = event.pos[1]
            mouse = Vector2(x, y)
            hover_guide = None
            for guide in self.dock_guides.values():
                guide_pos = guide.calcPosition()
                if mouse.distance(guide_pos) < 6:
                    hover_guide = guide
            if hover_guide != None:
                globvars.cargo_panel.setDock(hover_guide.object)
                globvars.cargo_panel.setDrawButtons(False)
                globvars.cargo_panel.show()


