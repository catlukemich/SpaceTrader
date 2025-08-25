from pygame.mixer import Sound

from cargo import createCargoArray
from view.sprite import *
from weapons import *

class Carrier(Sprite):

    def __init__(self, capacity = 500):
        Sprite.__init__(self, None)
        self.layer = 2
        self.weapon = Lasers([Vector2(-20,-10), Vector2(20,-10)]) # Has two lasers
        self.capacity = capacity
        self.cargos = createCargoArray()
        self.setRotation(0)
        self.setSpeed(0)
        self.accelerating = False
        self.decelerating = False
        self.rotating_left  = False
        self.rotating_right = False
        self.thrusters_sound = Sound("assets/sounds/thrusters.ogg")


    # Set rotation in degrees, where 0 is heading up:
    def setRotation(self, rotation):
        self.image          = self.getRotationHullImage(rotation)
        self.rockets_image  = self.getRotationThrustersImage(rotation)
        self.rotation = rotation


    def getRotationHullImage(self, rot):
        path = str(rot % 360)
        path = path.zfill(4)
        path = "assets/carrier_big/hull/" + path + ".png"
        image = assets.loadImage(path)
        return image

    def getRotationThrustersImage(self, rot):
        thruster_path = str(rot % 360)
        thruster_path = thruster_path.zfill(4)
        thruster_path = "assets/carrier_big/thrusters/" + thruster_path + ".png"
        thruster_image = assets.loadImage(thruster_path)
        return thruster_image

    def getImages(self):
        images = []
        for rot in range(0, 360):
            image = self.getRotationHullImage(rot)
            images.append(image)
        return images

    def draw(self):
        Sprite.draw(self)
        self.drawSelf()
        self.weapon.draw(self)

    def drawSelf(self):
        if self.accelerating:
            loc = globvars.viewport.project(self.position)
            loc.x = loc.x - self.image.get_width() / 2.0
            loc.y = loc.y - self.image.get_height() / 2.0
            globvars.surface.blit(self.rockets_image, (loc.x, loc.y))


    def getRotation(self):
        return self.rotation

    def setSpeed(self, speed):
        if speed >= -10:
            self.speed = speed
        else:
            self.speed = 0

    def getSpeed(self):
        return self.speed


    def setRockets(self, state):
        self.rockets_visible = state
        
    def setRotatingLeft(self, rotating):
        self.rotating_left = rotating

    def setRotatingRight(self, rotating):
        self.rotating_right = rotating

    def setAccelerating(self, acc):
        self.accelerating = acc
        if acc:
            self.thrusters_sound.play(-1)
        else:
            self.thrusters_sound.stop()

    def setDecelerating(self, dec):
        self.decelerating = dec
        if dec:
            self.thrusters_sound.play(-1)
        else:
            self.thrusters_sound.stop()

    def shoot(self):
        self.weapon.shoot(self) # Delegate the shot to the weapon

    def update(self, clock):
        self.manuever()
        self.weapon.update(clock)

    def manuever(self):
        if self.rotating_left:
            rot = self.getRotation()
            rot += 1
            self.setRotation(rot)
        if self.rotating_right:
            rot = self.getRotation()
            rot -= 1
            self.setRotation(rot)
        if self.accelerating:
            speed = self.getSpeed()
            speed += 0.2
            self.setSpeed(speed)
        if self.decelerating:
            speed = self.getSpeed()
            speed -= 0.2
            self.setSpeed(speed)



        rot = self.getRotation()
        fwd_vec = Vector2(0, -1)
        fwd_vec.rotate(rot)
        fwd_vec *= self.speed

        self.position += fwd_vec

    def getDescription(self):
        return ""

    def getPrice(self):
        return 0

    def clone(self):
        pass

    def getType(self):
        return ""

class SmallCarrier(Carrier):

    def __init__(self):
        Carrier.__init__(self, 300)

    def getRotationHullImage(self, rot):
        path = str(rot % 360)
        path = path.zfill(4)
        path = "assets/carrier_small/hull/" + path + ".png"
        image = assets.loadImage(path)
        return image

    def getRotationThrustersImage(self, rot):
        thruster_path = str(rot % 360)
        thruster_path = thruster_path.zfill(4)
        thruster_path = "assets/carrier_small/thrusters/" + thruster_path + ".png"
        thruster_image = assets.loadImage(thruster_path)
        return thruster_image


    def getDescription(self):
        return "Small carrier"

    def getPrice(self):
        return 20000

    def clone(self):
        return SmallCarrier()

    def getType(self):
        return "Small carrier"

class MediumCarrier(Carrier):

    def __init__(self):
        Carrier.__init__(self, 500)

    def getRotationHullImage(self, rot):
        path = str(rot % 360)
        path = path.zfill(4)
        path = "assets/carrier_medium/hull/" + path + ".png"
        image = assets.loadImage(path)
        return image

    def getRotationThrustersImage(self, rot):
        thruster_path = str(rot % 360)
        thruster_path = thruster_path.zfill(4)
        thruster_path = "assets/carrier_medium/thrusters/" + thruster_path + ".png"
        thruster_image = assets.loadImage(thruster_path)
        return thruster_image

    def getDescription(self):
        return "Medium carrier"

    def getPrice(self):
        return 30000

    def clone(self):
        return MediumCarrier()


    def getType(self):
        return "Medium carrier"


class BigCarrier(Carrier):

    def __init__(self):
        Carrier.__init__(self, 800)

    def getRotationHullImage(self, rot):
        path = str(rot % 360)
        path = path.zfill(4)
        path = "assets/carrier_big/hull/" + path + ".png"
        image = assets.loadImage(path)
        return image

    def getRotationThrustersImage(self, rot):
        thruster_path = str(rot % 360)
        thruster_path = thruster_path.zfill(4)
        thruster_path = "assets/carrier_big/thrusters/" + thruster_path + ".png"
        thruster_image = assets.loadImage(thruster_path)
        return thruster_image


    def getDescription(self):
        return "Heavy carrier"

    def getPrice(self):
        return 50000

    def clone(self):
        return BigCarrier()

    def getType(self):
        return "Big carrier"
