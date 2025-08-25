import pygame
from pygame.locals import *
import globvars
from main      import *
from mathutils import Vector2


class FlyHud:

    def __init__(self):
        self.dock_guides = {} # A map from a docks instances to docks guides
        self.shipyard_guides = {} # A map from a shipyards instances to shipyards guides


    def update(self):
        self.dock_guides = {}
        for dock in globvars.docks:
            dock_guide = HudGuide(dock)
            self.dock_guides[dock] = dock_guide

        self.shipyard_guides = { }
        for shipyard in globvars.shipyards:
            shipyard_guide = HudGuide(shipyard)
            self.shipyard_guides[shipyard] = shipyard_guide

        globvars.cargo_panel.update()


    def draw(self, nearby_dock, nearby_shipyard):
        ### NAVIGATION CIRCLE ###
        # Draw the navigation circle around the screen:
        pygame.draw.circle(globvars.surface, (200, 200, 200), (400, 400), 350, 2)

        for dock in self.dock_guides:
            dock_guide = self.dock_guides[dock]
            if dock is not nearby_dock:
                dock_guide.draw()
            
        for shipyard in self.shipyard_guides:
            shipyard_guide = self.shipyard_guides[shipyard]
            if shipyard is not nearby_shipyard:
                shipyard_guide.draw()

        font = pygame.font.Font("assets/gui/LCD14.ttf", 15)
        if nearby_dock != None:
            txt = font.render("Press \"D\" to enter " + nearby_dock.name + " spacedock.", 1, (255, 255, 255))
            globvars.surface.blit(txt, (220, 0))

        if nearby_shipyard != None:
            txt = font.render("Press \"ENTER\" to enter the shipyard.", 1, (255, 255, 255))
            globvars.surface.blit(txt, (220, 0))

        asteroids = globvars.asteroids
        for ast in asteroids:
            to_vec : Vector2 = ast.position - globvars.player.position
            distance_to_asteroid = to_vec.length()
            to_vec.normalize()
            additional_radius = map_value(distance_to_asteroid, 0, 5000, 0, 30)
            additional_radius = clamp(additional_radius, 0, 100)
            to_vec *= (240 + additional_radius)
            guide_pos = Vector2(400, 400)
            guide_pos += to_vec

            # Draw the guide of an asteroid:
            pygame.draw.circle(globvars.surface, (255, 0, 0), (int(guide_pos.x), int(guide_pos.y)), 4)


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



# Guide to any object in the world - is a mark within the navigation circle
# signifiying something distant.
class HudGuide:
    def __init__(self, object, show_distance = True, radius= 350, distance_min = 36000 , distance_max = 60000):
        self.object = object
        self.show_distance = show_distance
        self.distance_min = distance_min
        self.distance_max = distance_max
        self.radius = radius

    def draw(self):
        ### THE GUIDING POINT ###
        position = self.calcPosition()

        # Draw the guiding point to a planet:
        pygame.draw.circle(globvars.surface, (255, 255, 255), (int(position.x), int(position.y)), 4)
        font = pygame.font.Font("assets/gui/LCD14.ttf", 15)
        dist = int(globvars.player.position.distance(self.object.position))
        txt = font.render(self.object.name + " " + str(dist), 1, (255, 255, 255))

        # Draw the distance to a planet:
        globvars.surface.blit(txt, (position.x - 60, position.y))


    def calcPosition(self):
        ''' Calculate the screen position offset from the center of the view to the rim of the UI hud '''
        to_vec = self.object.position - globvars.player.position
        radius_min = self.radius - 50
        radius_max = self.radius + 50
        offset = map_value(to_vec.length(), self.distance_min, self.distance_max, radius_min, radius_max)
        offset = clamp(offset, radius_min, radius_max)
        
        to_vec.normalize()
        to_vec *= offset
        center_pos = Vector2(400, 400)
        center_pos += to_vec
        guide_pos = center_pos
        return guide_pos