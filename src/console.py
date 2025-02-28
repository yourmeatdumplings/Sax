#console
from pygame import Color


class Editor:
    Title: str = "Sax Editor"

class Display:
    WindowTitle: str = ''
    IsWindowFullScene: bool = False
    DefaultSize: tuple[int, int] = 1280, 720
    FullSceneSize: tuple[int, int] = 1920, 1080
    BGColor: str | tuple[int, int, int] | Color = 'black'