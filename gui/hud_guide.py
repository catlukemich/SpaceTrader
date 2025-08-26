import pygame
from pygame.locals import *
import globvars
from main      import *
from mathutils import Vector2, map_value


# Guide to any object in the world - is a mark within the navigation circle
# signifiying something distant.
class HudGuide:
    def __init__(self, object, radius= 350, distance_min = 36000 , distance_max = 60000):
        self.object = object
        self.show_distance = True
        self.distance_min = distance_min
        self.distance_max = distance_max
        self.radius = radius
        self.color = (255,255,255)

    def setColor(self, color):
        self.color = color
        return self
    
    def setShowDistance(self, show):
        self.show_distance = show
        return self

    def draw(self):
        ### THE GUIDING POINT ###
        position = self.calcPosition()

        # Draw the guiding point to a planet:
        pygame.draw.circle(globvars.surface, self.color, (int(position.x), int(position.y)), 4)
        if self.show_distance and hasattr(self.object, "name"):
            # Draw the distance to a planet:
            font = pygame.font.Font("assets/gui/LCD14.ttf", 15)
            dist = int(globvars.player.position.distance(self.object.position))
            txt = font.render(self.object.name + " " + str(dist), 1, self.color)
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
        center_pos = Vector2(
            globvars.surface.get_width() / 2, 
            globvars.surface.get_height() / 2
        )
        center_pos += to_vec
        guide_pos = center_pos
        return guide_pos