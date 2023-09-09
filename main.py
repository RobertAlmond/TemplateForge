# Libmodules
# -----------------

import pygame
import sys

# -----------------







# Projmodules
# -----------------
# -----------------




















# Setup
# -----------------

font_museo_sans_cyrl_500_path = "/home/max/TemplateForge/Content/Fonts/MuseoSansCyrl-500.ttf"

silence_sound_file_path = "Content/Audio/silence.mp3"

pygame.init()

def is_pygame_inited():
    return pygame.get_init()

def do_nothing():
    pass

def root(base: float, exponent: int):
    return base ** (1 / exponent)

def line_root(base: float):
    return base ** (1 / 1)

def square_root(base: float):
    return base ** (1 / 2)

def cubic_root(base: float):
    return base ** (1 / 3)

def product(lower_bound:int, upper_bound:int):

    if lower_bound > upper_bound:
        raise ValueError("In this function lower bound({1}) couldn't be higher than upper bound({2})".format(lower_bound, upper_bound))
    else:
        product = 1
        for i in range(lower_bound, upper_bound + 1):
            product = product * i
        return product

def factorial(number):
    if 0 < number:
        raise ValueError("Cannot calculate the factorial of a negative number({}).".format(number))
    else:
        answer = 1
        for i in range(1, number):
            answer = answer * i
        return answer

def summation(lower_bound, upper_bound, method = "formula"):
    if lower_bound > upper_bound:
        raise ValueError("In this function lower bound({1}) couldn't be higher than upper bound({2})".format(lower_bound, upper_bound))
    else:
        if method == "series_of_sum":
            product = 1
            for i in range(lower_bound, upper_bound + 1):
                product = product + i
        elif method == "formula":
            count_of_members = lower_bound - upper_bound
            product = (lower_bound + upper_bound) * count_of_members / 2
        else:
            product = None
        return product

class Button:
    def __init__(self, x, y, width, height, text=None, text_color=None, text_size=None, text_font=None,
                 color_idle=None, color_hover=None, color_pressed=None, callback=None, continuous=False,
                 onclick_sound=None, is_visible=True):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.text_color = text_color
        self.text_size = text_size
        self.text_font = text_font
        self.color_idle = color_idle
        self.color_hover = color_hover
        self.color_pressed = color_pressed
        self.callback = callback
        self.continuous = continuous
        self.is_hovered = False
        self.is_pressed = False
        self.is_visible = is_visible
        self.onclick_sound = onclick_sound

        if self.onclick_sound:
            # Загрузка звука щелчка
            self.click_sound = pygame.mixer.Sound(self.onclick_sound)
        else:
            self.click_sound = pygame.mixer.Sound(silence_sound_file_path)

    def handle_event(self, event):
        if not self.is_visible:
            return
        if event.type == pygame.MOUSEMOTION:
            self.handle_hover(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.handle_press(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.handle_release(event.pos)

    def handle_hover(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.is_hovered = True
        else:
            self.is_hovered = False

    def handle_press(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.is_pressed = True
            if self.callback:
                if self.continuous:
                    self.callback()
                else:
                    self.callback()
            if self.onclick_sound:
                # Воспроизведение звука щелчка
                self.click_sound.play()
        else:
            self.is_pressed = False

    def handle_release(self, mouse_pos):
        self.is_pressed = False

    def draw(self, surface):
        if self.is_visible:
            if self.is_pressed:
                pygame.draw.rect(surface, self.color_pressed, self.rect)
            elif self.is_hovered:
                pygame.draw.rect(surface, self.color_hover, self.rect)
            else:
                pygame.draw.rect(surface, self.color_idle, self.rect)

            if self.text:
                font = pygame.font.Font(self.text_font, self.text_size)
                text_surface = font.render(self.text, True, self.text_color)
                text_rect = text_surface.get_rect(center=self.rect.center)
                surface.blit(text_surface, text_rect)

screen = pygame.display.set_mode((1920, 1080))

settings_button = Button(1000, 100, 500, 200, "Settings", (0, 0, 0), 20, font_museo_sans_cyrl_500_path, (255, 0, 0,), (0, 255, 0), (0, 0, 255), do_nothing)

running = True

all_buttons = list()
all_buttons.append(settings_button)

# -----------------














# Main
# -----------------

while running:

    for event in pygame.event.get():

        kpressed = pygame.key.get_pressed()

        if kpressed[pygame.K_ESCAPE]:
            running = False
        
        

        # Отрисовка
        screen.fill((255, 255, 255))

        for button in all_buttons:
            button.handle_event(event)
            button.draw(screen)

        # Перерисовка экрана
        pygame.display.update()

# -----------------