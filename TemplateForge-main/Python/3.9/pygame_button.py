# Required modules: pygame

import pygame


class Button:
    def __init__(self, x, y,
                 width, height,
                 text_content=None, text_color=None, text_size=None, text_font=None,
                 color_idle=None, color_hover=None, color_pressed=None,
                 callback=None,
                 continuous=False,
                 onclick_sound=None,
                 is_visible=True):
        self.rect = pygame.Rect(x, y, width, height)
        self.text_content = text_content
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

            if self.text_content:
                font = pygame.font.Font(self.text_font, self.text_size)
                text_surface = font.render(self.text_content, True, self.text_color)
                text_rect = text_surface.get_rect(center=self.rect.center)
                surface.blit(text_surface, text_rect)
