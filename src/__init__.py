from src.Lib import *
from src.console import Display
from src.window import *
import pygame

class App:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption(window_title)
        pygame.display.set_mode(window_size, window_state)

        self.is_full = Display.IsWindowFullScene

        self.display_surface = pygame.display.get_surface()

        self.clock = pygame.time.Clock()

    def full_screen(self):
        if self.is_full:
            pygame.display.set_mode(Display.DefaultSize, 0)
        else:
            pygame.display.set_mode(Display.FullSceneSize, pygame.FULLSCREEN)

        self.is_full = not self.is_full

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tool.exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    self.full_screen()

    def update(self):
        self.clock.tick(60)
        self.display_surface.fill(Display.BGColor)
        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.update()