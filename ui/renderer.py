from utils import config

class Renderer:
    def __init__(self, screen, board, pygame):
        self.screen = screen
        self.board = board
        self.pygame = pygame

    def draw(self):
        self.board.draw_squares(self.screen, config, self.pygame)
