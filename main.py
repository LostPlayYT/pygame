import pygame

# Incializace pygame
pygame.init()


# Vytvoření obrazovky
width = 600
height = 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Naše první hra")

# Hlavní herní cyklus
lets_continue = True

while lets_continue:
    for event in pygame.event.get() :
        print(event)
        
        if event.type == pygame.QUIT:
            lets_continue = False 


# Ukončení pygame
pygame.quit()
