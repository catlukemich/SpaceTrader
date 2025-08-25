from mathutils import *
import globvars
import pygame
import assets
import random

class Sprite:

    def __init__(self, image = None, animation = None):
        self.position = Vector2()
        self.visible = True
        self.image = image
        self.animation = animation


    def update(self, clock):
        pass

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position

    def setVisible(self, visible):
        self.visible = visible
    
    def draw(self):
        if not self.visible: return # Dont draw the sprite if it's set to be invisible 

        pos = globvars.viewport.project(self.position)

        if self.animation != None:
            pos.x = pos.x - self.animation.frames[0].get_width() / 2.0
            pos.y = pos.y - self.animation.frames[0].get_height() / 2.0
            self.animation.draw(globvars.clock, pos)
        else:
            pos.x = pos.x - self.image.get_width() / 2.0
            pos.y = pos.y - self.image.get_height() / 2.0
            
            globvars.surface.blit(self.image, (pos.x, pos.y))


class Animation:

    def __init__(self, frames):
        self.frames = frames
        self.current_frame = 0
        self.last_time = 0
        self.frame_duration = 100 # 100 ms
        self.playing = False

    def draw(self, clock: pygame.time.Clock, pos):
        now = clock.get_time()
        time_elapsed =  self.last_time
        
        frame = (time_elapsed // self.frame_duration) % len(self.frames)
        if self.last_time + self.frame_duration > self.frame_duration * len(self.frames):
            self.playing = False
        else:
            globvars.surface.blit(self.frames[frame], (pos.x, pos.y))
        
        self.last_time += now

    def play(self):
        self.last_time = globvars.clock.get_time()
        self.playing = True






