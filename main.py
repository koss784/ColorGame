import pygame
from sys import exit

clock = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")

sky_surface = pygame.image.load("graphics/background.png").convert()
sky_surface = pygame.transform.rotozoom(sky_surface, 0, 1)


class RedBlock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("graphics/red_block.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=(300, 250))

    def update(self, *args, **kwargs):
        return super().update(*args, **kwargs)


red_block = pygame.sprite.Group()
red_block.add(RedBlock())


class BlueBlock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("graphics/blue_block.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=(300, 250))

    def update(self, *args, **kwargs):
        return super().update(*args, **kwargs)


blue_block = pygame.sprite.Group()
blue_block.add(BlueBlock())


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.base_image = pygame.image.load("graphics/Player.png").convert_alpha()
        self.image = self.base_image.copy()
        self.rect = self.image.get_rect(midbottom=(300, 100))

        self.gravity = 0
        self.color = pygame.Color("red")

    def change_color(self, color):
        self.color = color
        self.image = self.base_image.copy()
        self.image.fill(color, special_flags=pygame.BLEND_RGBA_MULT)

    def apply_gravity(self):
        self.gravity += 0.1
        self.rect.y += self.gravity

    def update(self):
        self.apply_gravity()


player = pygame.sprite.GroupSingle()
player.add(Player())


def CollisionBlockPlayer():
    if pygame.sprite.spritecollide(player.sprite, red_block, False):
        player.sprite.gravity = 0
        print("sosal")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        player.sprite.change_color(pygame.Color("White"))
        player.sprite.change_color(pygame.Color("Red"))
    if keys[pygame.K_2]:
        player.sprite.change_color(pygame.Color("Blue"))
    if keys[pygame.K_3]:
        player.sprite.change_color(pygame.Color("Green"))

    screen.blit(sky_surface, (0, -50))

    player.draw(screen)
    player.update()

    red_block.draw(screen)
    red_block.update()
    CollisionBlockPlayer()
    pygame.display.update()

    clock.tick(60)


#!MUST DO COLOR CHECK THING
