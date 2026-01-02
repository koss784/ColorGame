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


red_block = pygame.sprite.Group()
red_block.add(RedBlock())


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("graphics/Player.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=(300, 200))
        self.gravity = 0

    def apply_gravity(self):
        self.gravity += 0.1
        self.rect.y += self.gravity

    def update(self):
        self.apply_gravity()


player = pygame.sprite.GroupSingle()
player.add(Player())


def CollisionBlockPlayer():
 # !COLIDERECT SMTH

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, -50))

    player.draw(screen)
    player.update()

    red_block.draw(screen)

    pygame.display.update()

    clock.tick(60)
