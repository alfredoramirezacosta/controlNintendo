import pygame

pygame.init()

clk = pygame.time.Clock()

size = width, height = 960, 440
screen = pygame.display.set_mode(size)
background_image =pygame.image.load('control.png').convert()
frameRect = pygame.Rect((0, 0), (width, height))

crosshair = pygame.surface.Surface((10, 10))
pygame.draw.circle(crosshair, pygame.Color("black"), (5,5), 5, 0)

crosshairb = pygame.surface.Surface((10, 10))
pygame.draw.circle(crosshairb,pygame.Color("red"), (5,5), 5, 0)

while True:

    pygame.event.pump()

    screen.blit(background_image, (0, 0))

    Keys=pygame.key.get_pressed()

    if Keys[pygame.K_x]: screen.blit(crosshair, (700, 300))

    if Keys[pygame.K_a]: screen.blit(crosshair, (820, 300))

    if Keys[pygame.K_SPACE]: screen.blit(crosshair, (385, 300))

    if Keys[pygame.K_RETURN]: screen.blit(crosshair, (535, 300))

    x = "LEFT" if Keys[pygame.K_LEFT] else "RIGHT" if Keys[pygame.K_RIGHT] else ""

    y = "UP" if Keys[pygame.K_UP] else "DOWN" if Keys[pygame.K_DOWN] else ""

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(crosshairb,((int(x=='RIGHT')-int(x=='LEFT'))*65+177-5,(int(y=='DOWN')-int(y=='UP'))*65+272-5))

    pygame.display.flip()

    clk.tick(40)