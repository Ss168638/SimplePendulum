import pygame
import math
from colors import BLUE


class pendulam:
    def __init__(self, pendulumlen, gravity, color):
        self.origin = (300, 0)
        self.angle = math.pi/4
        self.angleofVelocity = 0
        self.angleofAccelaration = 0
        self.pendulumlen = pendulumlen
        self.gravity = gravity
        self.color = color
        self.pathtravelled = []

    def draw(self, win):
        force = self.gravity * math.sin(self.angle)
        self.angleofAccelaration = (-1 * force) / self.pendulumlen
        self.angleofVelocity += self.angleofAccelaration
        self.angle += self.angleofVelocity
        bob_x = self.pendulumlen * math.sin(self.angle) + self.origin[0]
        bob_y = self.pendulumlen * math.cos(self.angle) + self.origin[1]
        self.pathtravelled.append((bob_x, bob_y))
        pygame.draw.aaline(win, self.color, self.origin, (bob_x, bob_y))
        pygame.draw.circle(win, self.color, (bob_x, bob_y), 35)
        for path in self.pathtravelled:
            pygame.draw.line(win, self.color, path, (bob_x, bob_y))
        if self.pathtravelled.__len__() > 100:
            self.pathtravelled.pop(0)
