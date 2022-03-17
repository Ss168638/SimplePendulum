import pygame
from pendulam import pendulam
from colors import *
from slider import Slider

pygame.init()
WIDTH, HEIGHT = 600, 400
FRAME_RATE = 30

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
bobs = []
def get_bob(num):
    if num > 1:
        for number in range(0, num):
            bobs.append(pendulam(300, 1.0 * number, BLUE))
    else:
        bobs.append(pendulam(300, 1.0, BLUE))
    
def eventLoop():
    run = True
    clock = pygame.time.Clock()
    slider = Slider(0, HEIGHT-50, WIDTH, HEIGHT * 0.01)
    get_bob(1)
    while run:
        clock.tick(FRAME_RATE)
        WIN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                slider.handleEvent(WIN, pygame.mouse.get_pos()[0])
            
        speed = slider.getValue()
        for bob in bobs:
            bob.gravity = speed
            bob.draw(WIN)
        slider.draw(WIN)
        pygame.display.update()
    
    pygame.quit()


if __name__ == "__main__":
    eventLoop()