import math
import pygame
pygame.init()


def main():
    size = (700, 700)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Mandelbrot Set")

    clock = pygame.time.Clock()

    center = (size[0] // 2, size[1] // 2)

    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

main()
    
