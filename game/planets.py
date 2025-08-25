from view.sprite import *
from view.animated_sprite import *
from mathutils import *
from game.dock import *
from cargo import *

def createPlanetsWithDocks():
    scene = globvars.scene
    docks = globvars.docks

    # Planet 1 - Mercury:
    planet = Sprite(assets.loadImage("assets/planets/mercury.png"))
    planet.setPosition(Vector2(80000, 40000))
    scene.addSprite(planet)
    random.seed(0)
    dock = Dock()
    dock.setName("Mercury")
    dock.setPosition(Vector2(80000, 40000))
    dock.setCargoPrice(CARGO_1_NAME, 20)
    dock.setCargoAmount(CARGO_1_NAME, random.randint(300, 400))
    dock.addProducer(CargoProducer(CARGO_1_NAME, 10))
    dock.addConsumer(CargoConsumer(CARGO_2_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_3_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_4_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_5_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_6_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_7_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_8_NAME, 1))
    scene.addSprite(dock)
    docks.append(dock)

    # Planet 2 - Venus
    planet = Sprite(assets.loadImage("assets/planets/venus.png"))
    planet.setPosition(Vector2(30000, -43000))
    scene.addSprite(planet)
    random.seed(1)
    dock = Dock()
    dock.setName("Venus")
    dock.setPosition(Vector2(30000, -43000))
    dock.setCargoPrice(CARGO_2_NAME, 50)
    dock.setCargoAmount(CARGO_2_NAME, random.randint(300, 400))
    dock.addConsumer(CargoConsumer(CARGO_1_NAME, 1))
    dock.addProducer(CargoProducer(CARGO_2_NAME, 5))
    dock.addConsumer(CargoConsumer(CARGO_3_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_4_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_5_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_6_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_7_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_8_NAME, 1))
    scene.addSprite(dock)
    docks.append(dock)

    # Planet 3 - Earth
    planet = Sprite(assets.loadImage("assets/planets/earth.png"))
    planet.setPosition(Vector2(-3000, -3000))
    scene.addSprite(planet)
    random.seed(2)
    dock = Dock()
    dock.setName("Earth")
    dock.setPosition(Vector2(-3000, -3000))
    dock.setCargoPrice(CARGO_3_NAME, 60)
    dock.setCargoAmount(CARGO_3_NAME, random.randint(300, 400))
    dock.addConsumer(CargoConsumer(CARGO_1_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_2_NAME, 1))
    dock.addProducer(CargoProducer(CARGO_3_NAME, 5))
    dock.addConsumer(CargoConsumer(CARGO_4_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_5_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_6_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_7_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_8_NAME, 1))
    scene.addSprite(dock)
    docks.append(dock)

    # Planet 4 - Mars:
    planet = Sprite(assets.loadImage("assets/planets/mars.png"))
    planet.setPosition(Vector2(3000, -45000))
    scene.addSprite(planet)
    random.seed(3)
    dock = Dock()
    dock.setName("Mars")
    dock.setPosition(Vector2(3000, -45000))
    dock.setCargoPrice(CARGO_4_NAME, 80)
    dock.setCargoAmount(CARGO_4_NAME, random.randint(300, 400))
    dock.addConsumer(CargoConsumer(CARGO_1_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_2_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_3_NAME, 1))
    dock.addProducer(CargoProducer(CARGO_4_NAME, 5))
    dock.addConsumer(CargoConsumer(CARGO_5_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_6_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_7_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_8_NAME, 1))
    scene.addSprite(dock)
    docks.append(dock)

    # Planet 5 - Jupiter:
    planet = Sprite(assets.loadImage("assets/planets/jupiter.png"))
    planet.setPosition(Vector2(-83000, -30000))
    scene.addSprite(planet)
    random.seed(4)
    dock = Dock()
    dock.setName("Jupiter")
    dock.setPosition(Vector2(-83000, -30000))
    dock.setCargoPrice(CARGO_5_NAME, 80)
    dock.setCargoAmount(CARGO_5_NAME, random.randint(300, 400))
    dock.addConsumer(CargoConsumer(CARGO_1_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_2_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_3_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_4_NAME, 1))
    dock.addProducer(CargoProducer(CARGO_5_NAME, 10))
    dock.addConsumer(CargoConsumer(CARGO_6_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_7_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_8_NAME, 1))
    scene.addSprite(dock)
    docks.append(dock)

    # Planet 6 - Saturn:
    planet = Sprite(assets.loadImage("assets/planets/saturn.png"))
    planet.setPosition(Vector2(30000, 80000))
    scene.addSprite(planet)
    random.seed(5)
    dock = Dock()
    dock.setName("Saturn")
    dock.setPosition(Vector2(30000, 80000))
    dock.setCargoPrice(CARGO_6_NAME, 100)
    dock.setCargoAmount(CARGO_6_NAME, random.randint(300, 400))
    dock.addConsumer(CargoConsumer(CARGO_1_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_2_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_3_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_4_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_5_NAME, 1))
    dock.addProducer(CargoProducer(CARGO_6_NAME, 5))
    dock.addConsumer(CargoConsumer(CARGO_7_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_8_NAME, 1))
    scene.addSprite(dock)
    docks.append(dock)

    # Planet 7 - Uranus:
    planet = Sprite(assets.loadImage("assets/planets/uranus.png"))
    planet.setPosition(Vector2(-130000, 43000))
    scene.addSprite(planet)
    random.seed(6)
    dock = Dock()
    dock.setName("Uranus")
    dock.setCargoPrice(CARGO_7_NAME, 11.0)
    dock.setCargoAmount(CARGO_7_NAME, random.randint(300, 400))
    dock.addConsumer(CargoConsumer(CARGO_1_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_2_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_3_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_4_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_5_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_6_NAME, 1))
    dock.addProducer(CargoProducer(CARGO_7_NAME, 10))
    dock.addConsumer(CargoConsumer(CARGO_8_NAME, 1))
    dock.setPosition(Vector2(-130000, 43000))
    scene.addSprite(dock)
    docks.append(dock)

    # Planet 8 - Neptune:
    planet = Sprite(assets.loadImage("assets/planets/neptune.png"))
    planet.setPosition(Vector2(-53000, -63000))
    scene.addSprite(planet)
    random.seed(7)
    dock = Dock()
    dock.setName("Neptune")
    dock.setPosition(Vector2(-53000, -63000))
    dock.setCargoPrice(CARGO_8_NAME, 100)
    dock.setCargoAmount(CARGO_8_NAME, random.randint(300, 400))
    dock.addConsumer(CargoConsumer(CARGO_1_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_2_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_3_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_4_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_5_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_6_NAME, 1))
    dock.addConsumer(CargoConsumer(CARGO_7_NAME, 1))
    dock.addProducer(CargoProducer(CARGO_8_NAME, 5))
    scene.addSprite(dock)
    docks.append(dock)


def createAsteroids():
    for i in range(0, 40):
        asteroid = Asteroid()
        globvars.scene.addSprite(asteroid)
        globvars.asteroids.append(asteroid)


class Asteroid(AnimatedSprite):
    
    def __init__(self):
        variation = random.randint(1, 3)
        directory = "assets/asteroid" + str(variation)
        frames = assets.loadAnim(directory, 0, 99)
        AnimatedSprite.__init__(self, 4, frames)

        a, b = -100, 100
        rand_x = random.randint(a, b)
        rand_y = random.randint(a, b)
        pos = Vector2(rand_x, rand_y)
        self.setPosition(pos)

        vec_x = random.randint(-4, 4)
        vec_y = random.randint(-4, 4)
        self.vector = Vector2(vec_x, vec_y)

        t = random.randint(120, 160)
        self.timeout = t
        self.ticks = 0

        self.health = 100 + random.randint(0,20)
    

    def takeDamage(self, amount):
        self.health -= amount
        if self.health < 0:
            globvars.scene.removeSprite(self)
            if self in globvars.asteroids:
                globvars.asteroids.remove(self)

    def update(self, clock):
        AnimatedSprite.update(self, clock)
        self.position = self.position + self.vector
        self.ticks += 1
        if self.ticks % 60 == 0:
            self.timeout -= 1
        if self.timeout == 0:
            globvars.scene.removeSprite(self)
            globvars.asteroids.remove(self)
            new_asteroid = Asteroid()
            globvars.scene.addSprite(new_asteroid)
            globvars.asteroids.append(new_asteroid)

