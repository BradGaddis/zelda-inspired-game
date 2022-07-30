import pygame, sys
from level import Level
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((WIDTH, HEIGHT))
        window_icon = pygame.image.load(WINDOW_ICON)
        pygame.display.set_icon(window_icon)
        pygame.display.set_caption("Zelda's Version")
        self.clock = pygame.time.Clock()

        bg_music = pygame.mixer.music.load(FESTIVAL_BG_MUSIC_PATH)
        pygame.mixer.music.play(-1)

        self.current_level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.current_level.run()
            

if __name__ == "__main__":
    game = Game()
    game.run()