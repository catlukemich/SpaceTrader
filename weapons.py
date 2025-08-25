import abc
import random

import assets
import pygame
import globvars # For viewport
from mathutils import Vector2
from view.sprite import Animation, Sprite # For directional weapons

class Weapon:
    '''
    Weapon is the base class of every weapon present and available in the game.
    '''    

    def __init__(self):
        self.damage = 1 # A number
        self.shot = False # A flag indicating if the weapon was shot

    def takeDamage(self, object_hit):
        object_hit.life -= self.damage

    @abc.abstractmethod
    def shoot(self, from_ship):
        pass

    @abc.abstractmethod
    def update(self, clock):
        pass
    
    @abc.abstractmethod
    def draw(self, for_ship):
        pass

    def getSpaceEntities(self):
        ''' Convenience method for obtaining things that can be shot down '''
        entities = [globvars.spaceships, globvars.shipyards, globvars.asteroids, globvars.docks]
        flat = [x for sublist in entities for x in sublist]
        return flat

class Lasers(Weapon):
    '''
    Lasers. Every every ship can mount multiple laser beams. 
    The lasers can shoot infinitely into space, while with increasing distance - their power decrease.
    '''

    def __init__(self, mount_points):
        self.mount_points = mount_points # Mount points of the lasers
        self.duration = 200 # In ms
        self.iterations = 0
        self.shot = False


    def shoot(self, from_ship):
        self.shot = True
        self.iterations = 0
        laser_beep = assets.loadSound("assets/sounds/laser.ogg")
        laser_beep.play()

        # Check if we shot something
        entities = self.getSpaceEntities()
        own_position : Vector2 = from_ship.getPosition()
        for mount_point in self.mount_points:
            # We shoot from as many mountpoints as the weapon is mounted onto the ship
            for entity in entities:
                if entity == from_ship: continue
                # entity = globvars.shipyards[0]
                # See if we hit any entity
                entity_position : Vector2 = entity.getPosition()

                rot = from_ship.getRotation()
                fwd_vec = Vector2(0, -1)
                fwd_vec.rotate(rot)
                fwd_vec.normalize()
                start_point : Vector2 =  own_position + mount_point.rotated(rot)
                
                shoot_vector = fwd_vec * 900
                line_distance = start_point.distancePointToLine(shoot_vector, entity_position)
                if line_distance < 50:
                    distance_to_entity = own_position.distance(entity_position)
                    if distance_to_entity < 900:
                        self.playExplosion(entity)
                        if hasattr(entity, "takeDamage"): # Duck typing heeree
                            entity.takeDamage(60)


    def playExplosion(self, entity : Sprite):
        ''' Make the explosions and make the shot entity to get some damage. '''
        anim = Animation(assets.loadAnim("assets/effects/explosion-1", 0, 15))
        spr = Sprite(animation=anim)
        globvars.scene.addSprite(spr)
        
        # Play the explosion animation that's offset by a little bit #
        entity_pos = entity.getPosition()
        explosion_position = Vector2(entity_pos.x + random.randint(-10,10), entity_pos.y + random.randint(-10,10))
        spr.setPosition(explosion_position)
        anim.play()
        # Play the explosion sound TODO randomly modulate the sound volume #
        assets.loadSound("assets/sounds/explosion-1.wav").play()


    def update(self, clock):
        self.iterations += 1
        if self.iterations > 30:
            self.shot = False

    def draw(self, for_ship):
            if self.shot:
                for mount_point in self.mount_points:
                    rot = for_ship.getRotation()
                    fwd_vec = Vector2(0, -1)
                    fwd_vec.rotate(rot)
                    fwd_vec.normalize()
                    ship_screen_pos = globvars.viewport.getScreenCenter()
                    start_point =  ship_screen_pos + mount_point.rotated(rot)
                    shoot_vector = fwd_vec * 900
                    end_vector = ship_screen_pos + shoot_vector

                    width_divisor = self.iterations / 30 * 5
                    if width_divisor > 5:
                        width_divisor = 5
                    pygame.draw.line(globvars.surface, (255,0,0), start_point.asTuple(), end_vector.asTuple(), int(5 / width_divisor))