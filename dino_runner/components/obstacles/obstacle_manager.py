import pygame
import random
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import HAMMER_TYPE, SHIELD_TYPE


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def generator_obstacles(self,variable_obstacle):
        if variable_obstacle == 0:
            Cactus_type = "SMALL"
            obstacle = Cactus(Cactus_type)

        elif variable_obstacle == 1:
             Cactus_type = "LARGE"
             obstacle = Cactus(Cactus_type)

        elif variable_obstacle == 2:
             obstacle = Bird()
        return obstacle


    def update(self, game_speed, game):
        
        if len(self.obstacles) == 0:
            variable_obstacle = random.randint(0,2)
            obstacle = self.generator_obstacles(variable_obstacle)
            self.obstacles.append(obstacle)

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                
                if game.player.type == SHIELD_TYPE:
                    pass
                elif game.player.type == HAMMER_TYPE:  
                    self.obstacles.pop()

                elif game.heart_manager.heart_count < 1 :
                    pygame.time.delay(300)
                    game.playing = False
                    break
                else: 
                    game.heart_manager.reduce_heart()
                    self.obstacles.pop()           

                
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)