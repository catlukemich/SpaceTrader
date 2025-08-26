import abc
import random
import assets
import pygame
import globvars
from mathutils import Vector2
from view.sprite import Animation, Sprite # For directional weapons

class Weapon:
    '''
    Weapon is the base class of every weapon present and available in the game.
    '''    

    def __init__(self):
        self.damage = 1 # A number
        self.shot = False # A flag indicating if the weapon was shot

    @abc.abstractmethod
    def shoot(self, from_ship):
        ''' 
        Shoot the weapon from the ship 
        :param from_ship: The ship from which the weapon is being shot
        '''
        pass

    @abc.abstractmethod
    def update(self, clock):
        ''' 
        Update the state of the weapon 
        :param clock The clock that can be used during the update
        '''
        pass
    
    @abc.abstractmethod
    def draw(self, for_ship):
        '''
        Draw the weapon for a specified ship - it's up to implementation 
        how the weapon is drawn in time and spatially.
        :param for_ship The ship for which the weapon is drawn.
        '''
        pass

    def entityInFront(self, for_ship, entity):
        ''' 
        Convenience method for checking if the ship is heading toward another entity.
        In practice this means that the ship is directed so that it has the entity 
        within 180 degrees angle in front.
        :param for_ship Check the heading of this ship
        :param entity Check if the ship is heading toward this entity
        '''
        position : Vector2 = for_ship.getPosition()
        entity_pos = entity.getPosition()
        to_vec = entity_pos - position
        to_vec.normalize()
        heading = for_ship.getHeading()
        return to_vec.dot(heading) > 0


    def getSpaceEntities(self):
        ''' Convenience method for obtaining things that can be shot down in the world - the space'''
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

                rotation = from_ship.getRotation()
                fwd_vec = from_ship.getHeading()
                
                start_point : Vector2 =  own_position + mount_point.rotated(rotation)
                shoot_vector = fwd_vec * 900
                line_distance = start_point.distancePointToLine(shoot_vector, entity_position)
                if line_distance < 50:
                    distance_to_entity = own_position.distance(entity_position)
                    if distance_to_entity < 900 and self.entityInFront(from_ship, entity):
                        self.playExplosion(entity)
                        if hasattr(entity, "takeDamage"): # Duck typing heeree
                            entity.takeDamage(60)


    def playExplosion(self, entity : Sprite):
        ''' 
        Make the explosions and make the shot entity to get some damage. 
        :param entity The entity at which the explosion has to apear
        '''
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


    def update(self, clock = None):
        ''' Update the the lasers - make them apear for a while '''
        self.iterations += 1
        if self.iterations > 30:
            self.shot = False

    def draw(self, for_ship):
            if self.shot:
                for mount_point in self.mount_points:
                    rotation = for_ship.getRotation()
                    fwd_vec = for_ship.getHeading()
                    ship_screen_pos = globvars.viewport.getScreenCenter()
                    start_point =  ship_screen_pos + mount_point.rotated(rotation)
                    shoot_vector = fwd_vec * 900
                    end_vector = ship_screen_pos + shoot_vector

                    width_divisor = self.iterations / 30 * 5
                    if width_divisor > 5:
                        width_divisor = 5
                    pygame.draw.line(globvars.surface, (255,0,0), start_point.asTuple(), end_vector.asTuple(), int(5 / width_divisor))