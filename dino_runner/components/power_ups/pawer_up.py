from pygame.scrap import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH


class PowerUP(Sprite):

    def __init__(self, imaage, type):
        print("power")
        self.image = imaage
        self.type = type
        self.rect = self.image.get_reat()
        self.rect.y = 125
        self.rect.x = SCREEN_WIDTH

def update(self, game_speed, powerups):
    self.rect.x -= game_speed

    if self.rect.x < 0:
        powerups.pop()

def draw(self, screen):
    screen.blit(self.image, self.rect)