import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption('Serenity')

clock = pygame.time.Clock()

score_font = pygame.font.Font('graphics/Fonts/DungeonFont.ttf', 50)

sky_surface = pygame.image.load('graphics/backgrounds/platformer_background_3/layers/layer07_Sky.png')
ground_surface = pygame.image.load('graphics/Backgrounds/platformer_background_3/Layers/layer01_Ground.png')

score_surface = score_font.render('My Game', False, 'Black')
score_rect = score_surface.get_rect(midbottom = (500, 50))

bat_surface = pygame.image.load('graphics/Enemies/Bat/Idle/Bat Idle.gif').convert_alpha()
bat_rect = bat_surface.get_rect(midbottom = (900,630))
bat_enemy = (bat_surface,bat_rect)

player_surf = pygame.image.load('graphics/Player/Blue_witch/witch_idle1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (100,630))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #if event.type == pygame.MOUSEMOTION:
            #if player_rect.collidepoint(event.pos): print('collision')

    bat_rect.x -= 4
    if bat_rect.right <= 0: bat_rect.left = 800
    screen.blit(sky_surface,(0, 0))
    screen.blit(ground_surface,(-200,-300))
    screen.blit(score_surface,score_rect)

    if player_rect.colliderect(bat_rect):
        print('collision')

    #mouse_pos = pygame.mouse.get_pos()
    #if player_rect.collidepoint(mouse_pos):
        #print(pygame.mouse.get_pressed())

    screen.blit(bat_surface,bat_rect)
    screen.blit(player_surf,player_rect)
    pygame.display.update()
    clock.tick(60)