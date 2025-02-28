from src.console import Editor, Display
import pygame

window_title = Display.WindowTitle if Display.WindowTitle else Editor.Title
window_size = Display.FullSceneSize if Display.IsWindowFullScene else Display.DefaultSize
window_state = pygame.FULLSCREEN if Display.IsWindowFullScene else 0