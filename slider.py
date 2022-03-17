import pygame
from colors import *
class Slider:
    def __init__(self, qx, qy, w, h):
        self.circle_x = qx
        self.value = 0
        self.sliderRect = pygame.Rect(qx, qy, w, h)
        self.colorRect = RED
        self.colorCircle = WHITE

    def draw(self, win):
        pygame.draw.rect(win, self.colorRect, self.sliderRect)
        pygame.draw.circle(win, self.colorCircle, (self.circle_x, (self.sliderRect.h/2 + self.sliderRect.y)), self.sliderRect.h * 1.5)

    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value

    def updateValue(self, value):
        if value < self.sliderRect.x:
            self.value = 0
        elif value > self.sliderRect.x + self.sliderRect.w:
            value = 100
        else:
            self.value = int(((value - self.sliderRect.x)/self.sliderRect.w) * 100)

    def onSlider(self, x, y):
        if self.on_slider_hold(x, y) or self.sliderRect.x <= x <= self.sliderRect.x + self.sliderRect.w and self.sliderRect.y <= y <= self.sliderRect.y + self.sliderRect.h:
            return True
        else:
            return False
    
    def on_slider_hold(self, x, y):
        if ((x - self.circle_x) * (x - self.circle_x) + (y - (self.sliderRect.y + self.sliderRect.h / 2)) * (y - (self.sliderRect.y + self.sliderRect.h / 2)))\
            <= (self.sliderRect.h * 1.5) * (self.sliderRect.h * 1.5):
            return True
        else:
            return False

    def handleEvent(self, win, qx):
        if qx < self.sliderRect.x:
            self.circle_x = self.sliderRect.x
        elif qx > self.sliderRect.x + self.sliderRect.w:
            self.circle_x = self.sliderRect.x + self.sliderRect.w
        else:
            self.circle_x = qx
        if self.on_slider_hold(qx, self.sliderRect.y) == True:
            self.draw(win)
        self.updateValue(qx)
        
