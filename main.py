import pygame

# Incializace pygame
pygame.init()


# Vytvoření obrazovky
width = 600
height = 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Naše první hra")

player = pygame.Rect((300, 250, 50, 50))

# Hlavní herní cyklus
lets_continue = True

fps = pygame.time.Clock()

while lets_continue:
    screen.fill((0, 0, 0))
    
    pygame.draw.rect(screen,(255, 0, 0), player)

    key = pygame.key.get_pressed()

    if (key[pygame.K_a] or key [pygame.K_LEFT]) and player.left > 0:
        player.move_ip(-1,0)

    if (key[pygame.K_d] or key [pygame.K_RIGHT]) and player.right < width:
        player.move_ip(1,0)

    if (key[pygame.K_w] or key [pygame.K_UP]) and player.top > 0:
        player.move_ip(0,-1)

    if (key[pygame.K_s] or key [pygame.K_DOWN]) and player.bottom < height:
        player.move_ip(0,1)
    
    elif key[pygame.K_r] == True:
        player = pygame.Rect((300, 250, 50, 50))
 
    
    for event in pygame.event.get() :
        print(event)
        
        if event.type == pygame.QUIT:
            lets_continue = False 

    pygame.display.update()

    fps.tick(100)

# Ukončení pygame
pygame.quit()
