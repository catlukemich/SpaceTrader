from mathutils import *
import globvars

class Scene:
    def __init__(self):
        self.sprites = []
        self.iterating = False
        self.marked_for_removal = []

    def addSprite(self, sprite):
        self.sprites.append(sprite)
        
    def addSprites(self, sprites):
        self.sprites.extend(sprites)

    def removeSprite(self, sprite):
        if self.iterating:
            self.marked_for_removal.append(sprite)
        else:
            if sprite in self.sprites:
                self.sprites.remove(sprite)

    def update(self, clock):
        self.iterating = True
        for sprite in self.sprites:
            sprite.update(clock)
        self.iterating = False

        for marked in self.marked_for_removal:
            self.sprites.remove(marked)
        self.marked_for_removal.clear()
            

class Viewport:

    def __init__(self, width, height):
        self.center = Vector2()
        self.width  = width
        self.height = height
    
    def project(self, vec2):
        ''' 
        Project world position to the screen position, this includes the center of the screen 
        TODO For now the center of the screen is at (0, 0) ?
        '''
        result = vec2 - self.center

        result.x += self.width  / 2
        result.y += self.height / 2
            
        return result    

    def getScreenCenter(self):
        result = Vector2()

        result.x += self.width  / 2
        result.y += self.height / 2
        return result

    def draw(self):
        from functools import cmp_to_key
        # globvars.scene.sprites.sort(key = cmp_to_key(lambda a, b: a.layer - b.layer))

        for sprite in globvars.scene.sprites:
            sprite.draw()
