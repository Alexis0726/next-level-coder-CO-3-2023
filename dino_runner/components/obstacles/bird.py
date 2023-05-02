import random
from dino_runner.components.obstacles.obstaacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    def __init__(self):
        self.type = 0
        super().__init__(BIRD,self.type)
        self.rect.y = random.randint(200, 300)
        self.step = 0
        
    def draw(self, screen):
        if self.step >= 9:
            self.step = 0
        screen.blit(BIRD[self.step//5], self.rect)
        self.step += 1
    
