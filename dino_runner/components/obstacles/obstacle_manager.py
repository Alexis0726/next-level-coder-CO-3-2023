import pygame
import random
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus


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
                pygame.time.delay(300)
                game.playing = False
                break
    

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)