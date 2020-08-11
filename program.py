"""
Draw items on your screen
Play sound effects and music
Handle user input
Implement event loops
Describe how game programming differs from standard procedural Python programming
"""
import pygame

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])


def main():
    running = True
    while running:
        # user wants to quit ?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

        pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
