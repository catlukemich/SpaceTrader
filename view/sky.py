from .sprite import *

SKY_SIZE = 800

class Sky(Sprite):

    def __init__(self):
        Sprite.__init__(self, None)
        w = SKY_SIZE
        h = SKY_SIZE
        self.image = pygame.Surface((w, h), pygame.SRCALPHA)
        img = self.image

        for i in range(0,2000):
            x = random.randint(0, w )
            y = random.randint(0,h)
            r = random.randint(1,2)
            bright = random.randint(0,255)
            pygame.draw.rect(img, (bright, bright, bright), (x, y,r,r))

    def draw(self):
        player_pos = globvars.player.getPosition()

        SKY_SIZE_LOCAL = SKY_SIZE 

        offset_x = map_value(player_pos.x, 30000, -30000, -SKY_SIZE, SKY_SIZE)
        offset_y = map_value(player_pos.y, 30000, -30000, -SKY_SIZE, SKY_SIZE)

        offset_x = offset_x % SKY_SIZE_LOCAL
        offset_y = offset_y % SKY_SIZE_LOCAL

        for row in range(0,9):
            for col in range(0,9):
                globvars.surface.blit(self.image, (offset_x + col * SKY_SIZE_LOCAL - 1800, offset_y + row * SKY_SIZE_LOCAL - 1800))



