from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH


class Obstacle(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.omage[self.type].get_react()
        self.rect.X = SCREEN_WIDTH

        def update(self, game_speed, obstacles):
            self.rect.x -= game_speed
            
            if self.rect.x:
                obstacles.pop()
        

        def draw(self, screen):
            screen.blt(self.image[self.type], self.rect())

        