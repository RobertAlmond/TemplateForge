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

pygame.init()
pygame.font.init()

font_museo_sans_cyrl_500_path = "/home/max/TemplateForge/Content/Fonts/MuseoSansCyrl-500.ttf"
font_museo_sans_cyrl_500 = pygame.font.Font(font_museo_sans_cyrl_500_path, 20,)

silence_sound_file_path = "Content/Audio/silence.mp3"

def is_pygame_inited():
    return pygame.get_init()

def is_pygame_font_inited():
    return pygame.font.get_init()

def do_nothing():
    pass

def settings_button_func():
    back_to_main_menu_from_settings_button.is_visible = True
    about_button.is_visible = False
    settings_button.is_visible = False

def back_to_main_menu_from_settings_button_func():
    back_to_main_menu_from_settings_button.is_visible = False
    settings_button.is_visible = True
    about_button.is_visible = True

def about_button_func():
    settings_button.is_visible = False
    about_button.is_visible = False
    back_to_main_menu_from_about_button.is_visible = True
    contact_info_text1.is_visible = True
    contact_info_text2.is_visible = True
    contact_info_text3.is_visible = True

def back_to_main_menu_from_about_button_func():
    back_to_main_menu_from_about_button.is_visible = False
    settings_button.is_visible = True
    about_button.is_visible = True
    contact_info_text1.is_visible = False
    contact_info_text2.is_visible = False
    contact_info_text3.is_visible = False




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
        raise ValueError("In this function lower_bound({1}) couldn't be higher than upper_bound({2})".format(lower_bound, upper_bound))
    else:
        product = 1
        for i in range(lower_bound, upper_bound + 1):
            product *= i

        return product



def factorial(number:int):

    if number < 0:
        raise ValueError("In this function argument 'number' couldn't be higher than 0")
    elif number == 0:
        return 1
    else:
        answer = 1
        for i in range(1, upper_bound + 1):
            product *= i

        return product

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

settings_button = Button(
x = 100,
y = 100,
width = 250,
height = 110,
text = "Settings",
text_color = (0, 0, 0),
text_size = 35,
text_font = font_museo_sans_cyrl_500_path,
color_idle = (255, 0, 0),
color_hover = (0, 255, 0),
color_pressed = (0, 0, 0),
callback = settings_button_func,
)

about_button = Button(
x = 100,
y = 600,
width = 250,
height = 110,
text = "About",
text_color = (0, 0, 0),
text_size = 35,
text_font = font_museo_sans_cyrl_500_path,
color_idle = (255, 0, 0),
color_hover = (0, 255, 0),
color_pressed = (0, 0, 0),
callback = about_button_func,
)

back_to_main_menu_from_settings_button = Button(
x = 700,
y = 100,
width = 250,
height = 110,
text = "Back",
text_color = (0, 0, 0),
text_size = 35,
text_font = font_museo_sans_cyrl_500_path,
color_idle = (255, 0, 0),
color_hover = (0, 255, 0),
color_pressed = (0, 0, 0),
callback = back_to_main_menu_from_settings_button_func,
)

back_to_main_menu_from_about_button = Button(
x = 500,
y = 100,
width = 250,
height = 110,
text = "Back",
text_color = (0, 0, 0),
text_size = 35,
text_font = font_museo_sans_cyrl_500_path,
color_idle = (255, 0, 0),
color_hover = (0, 255, 0),
color_pressed = (0, 0, 0),
callback = back_to_main_menu_from_about_button_func,
)


contact_info_text1 = Text(
x = 500,
y = 500,
text = """Contact information:""",
size=80,
font=font_museo_sans_cyrl_500,
color=(0, 0, 0),
antialias=True,
is_visible=False,
)

contact_info_text2 = Text(
x = 500,
y = 600,
text = """Gmail: robertalmond.3ua@gmail.com""",
size=80,
font=font_museo_sans_cyrl_500,
color=(0, 0, 0),
antialias=True,
is_visible=False,
)

contact_info_text3 = Text(
x = 500,
y = 650,
text = """Telegram: @Almond001""",
size=80,
font=font_museo_sans_cyrl_500,
color=(0, 0, 0),
antialias=True,
is_visible=False,
)
running = True
back_to_main_menu_from_settings_button.is_visible = False
back_to_main_menu_from_about_button.is_visible = False

all_buttons = list()
all_texts = list()

all_buttons.append(settings_button)
all_buttons.append(back_to_main_menu_from_settings_button)
all_buttons.append(about_button)
all_buttons.append(back_to_main_menu_from_about_button)

all_texts.append(contact_info_text1)
all_texts.append(contact_info_text2)
all_texts.append(contact_info_text3)
# -----------------














# Main
# -----------------

print(is_pygame_font_inited())

while running:

    for event in pygame.event.get():

        kpressed = pygame.key.get_pressed()

        if kpressed[pygame.K_ESCAPE]:
            running = False

        screen.fill((255, 255, 255))

        for button in all_buttons:
            button.handle_event(event)
            button.draw(screen)

        for text in all_texts:
            text.draw(screen)

        pygame.display.update()

# -----------------
