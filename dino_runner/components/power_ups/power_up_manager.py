import random
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer

class PowerUpManager:

    def __init__(self):
        self.power_ups = []
        self.points = 0
        self.when_appears = 0


    def generate_power_ups(self, points):
        self.points = points

        if len(self.power_ups) == 0:
            power_up_type = random.randint(0,1)
            if self.when_appears == self.points:
                print("generating power up")
                if power_up_type == 0:
                    power_up = self.select_power_up(power_up_type)
                    self.power_ups.append(power_up)
                    self.when_appears += random.randint(200, 500)
        
                elif power_up_type == 1:
                    power_up = self.select_power_up(power_up_type)
                    self.power_ups.append(power_up)
                    self.when_appears += random.randint(200, 500)

    def update(self, points, game_speed, player):
        self.generate_power_ups(points)
        
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                start_time = pygame.time.get_ticks()
                time_random = random.randrange(5,8)
                player.has_power_up = True
                player.type = power_up.type
                player.power_time_up = start_time + (time_random * 1000)
                self.power_ups.pop()
                

    def select_power_up(self, power_up_type):
        if power_up_type == 0:
            power_up = Shield()
        elif power_up_type == 1: 
            power_up = Hammer()

        return power_up

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)