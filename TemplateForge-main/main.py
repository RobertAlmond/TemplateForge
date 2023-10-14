import pygame

def factorial(number: int) -> int:
    if not isinstance(number, int):
        raise TypeError("Argument 'number' must be an integer.")
    elif number < 0:
        raise ValueError(
            "Argument 'number' must be a non-negative integer. "
        )

    elif number == 0:
        return 1

    else:
        answer = 1
        for i in range(1, number + 1):
            answer *= i
        return answer


class Text:
    def __init__(self,
                 x=0,
                 y=0,
                 text="",
                 size=10,
                 font=None,
                 color=(0, 0, 0),
                 antialias=True,
                 is_visible=True):
        self.x = x
        self.y = y
        self.text = text
        self.size = size
        self.font = font or pygame.font.SysFont("arial", size)
        self.color = color
        self.antialias = antialias
        self.is_visible = is_visible

        self.surface = pygame.font.Font.render(self.font, self.text, self.antialias, self.color)
        self.rect = self.surface.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, surface):
        if self.is_visible:
            surface.blit(self.surface, self.rect)

    def set_position(self, x, y):
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y

    def set_text(self, text):
        self.text = text
        self.surface = self.font.render(self.text, self.antialias, self.color)
        self.rect = self.surface.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def set_font(self, font):
        self.font = font
        self.surface = self.font.render(self.text, self.antialias, self.color)
        self.rect = self.surface.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def set_size(self, size):
        self.size = size
        self.font = pygame.font.SysFont("arial", size)
        self.surface = self.font.render(self.text, self.antialias, self.color)
        self.rect = self.surface.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def set_color(self, color):
        self.color = color
        self.surface = self.font.render(self.text, self.antialias, self.color)
        self.rect = self.surface.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def set_antialias(self, antialias):
        self.antialias = antialias
        self.surface = self.font.render(self.text, self.antialias, self.color)
        self.rect = self.surface.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y