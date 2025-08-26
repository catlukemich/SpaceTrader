from .gui import *

class SpeedGauge(Text):

    def __init__(self):
        Text.__init__(self, pygame.font.Font("assets/gui/LCD14.ttf", 15))

    def update(self, clock):
        self.setText(f"Speed: {globvars.player.getSpeed():.2f}")