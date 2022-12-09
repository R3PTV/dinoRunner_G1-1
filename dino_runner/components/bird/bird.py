import random
from dino_runner.utils.constants import SCREEN_WIDTH, BIRD
#from dino_runner.components.obstacle.obstacle import Obstacle

class Bird():
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800,3000)
        self.y = random.randint(200, 340)
        self.image = BIRD[0]
        self.width = self.image.get_width()
        self.step_index = 1 
        self.bird_rect = self.image.get_rect()
        self.bird_rect.x = self.x
        self.bird_rect.y = self.y

    def update(self, game):
        self.x -=game.game_speed
        self.bird_animation()
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(200,340)
        
        if self.step_index >= 10:
            self.step_index = 0
        

    def bird_animation(self):
        self.image = BIRD[0] if self.step_index <5 else BIRD[1]
        self.bird_rect = self.image.get_rect()
        self.bird_rect.x = self.x
        self.bird_rect.y = self.y
        self.step_index += 1

    def draw(self, screen):
        screen.blit(self.image, (self.bird_rect.x, self.bird_rect.y))