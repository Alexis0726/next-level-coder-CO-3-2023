from dino_runner.utils.constants import HEART


class Heart:
    def __init__(self, pos_x, pos_y):
        self.image = HEART
        self.rect = self.image.get_rect()
        self.pos_x = pos_x
        self.pos_y = pos_y

    def draw(self,screen):
        screen.blit(self.image, self.rect)