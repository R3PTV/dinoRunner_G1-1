import pygame
import random
from dino_runner.components.obstacle.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
#from dino_runner.components.bird.bird import Bird

class ObstacleManager():
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0,1) == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            if random.randint(0,1) == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            #self.obstacles.append(Cactus(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle):
                pygame.time.delay(500)
                #game.playing - False
                #break
                #game.death_count = game.death_count +1
                #pygame.time.delay(100)
                #self.obstacle =[]

                if not game.player.shield:
                    
                    game.player_heart_manager.reduce_heart()
                    if game.player_heart_manager.heart_count >0:
                        game.player.show_text = False
                        game.player.shield = True
                        start_time = pygame.time.get_ticks()
                        game.player.shield_time_up = start_time +1000
                    
                    else:
                        pygame.time.delay(500)
                        game.playing = False
                        game.death_count = game.death_count +1
                        break
                else:
                    self.obstacles.remove(obstacle)

 ##       if self.step_index >= 10:
   #         self.step_index = 0





    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacle(self, self1):
        self.obstacle = []