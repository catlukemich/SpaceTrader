from view.sprite_group import *
from view.animated_sprite import *
import assets

class Shipyard(SpriteGroup):

    def __init__(self):
        SpriteGroup.__init__(self)

        self.name = "Shipyard" # Field required by FlyHud to display guide name.

        frames = assets.loadAnim("assets/shipyard/station", 0, 9)
        self.station = AnimatedSprite(6, frames)
        self.addSprite(self.station)

        frames = assets.loadAnim("assets/shipyard/robot",0 , 40)
        self.robot = AnimatedSprite(10, frames)
        self.addSprite(self.robot)

        self.setPosition(Vector2(-3350, -3001))