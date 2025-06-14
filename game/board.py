class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def draw_squares(self, screen, config, pygame):
        for row in range(config.ROWS):
            for col in range(config.COLS):
                color = config.WHITE if (row + col) % 2 == 0 else config.BROWN
                pygame.draw.rect(screen, color, (col * config.SQUARE_SIZE, row * config.SQUARE_SIZE,
                                                 config.SQUARE_SIZE, config.SQUARE_SIZE))
