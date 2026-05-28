import pygame

class Earth:
    def __init__(self, mass):
        self.x = 400
        self.y = 300
        self.radius = 20
        self.mass = mass

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), (int(self.x), int(self.y)), self.radius)

    def update(self):
        print("<", self.x, ",",self.y, ">")