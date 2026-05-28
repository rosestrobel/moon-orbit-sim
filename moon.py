import pygame

class Moon:
    def __init__(self, x, y, radius, mass):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = -2.0
        self.radius = radius
        self.mass = mass

    def update(self, ax, ay):
        self.vx += ax
        self.vy += ay
        self.x += self.vx
        self.y += self.vy
        # return self.x, self.y
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius)
