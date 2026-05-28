import pygame
from pygame import *
import moon
import earth
import math

pygame.init()

# WINDOW CONSTANTS

WIDTH, HEIGHT = 800, 600
screen = display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moon Orbit Simulation")
clock = pygame.time.Clock()



# SIMULATION PARAM

GRAVITY = 0.5
VELOCITY = 0.1

def getCenterDistance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculateGravitation(m1, m2, r):
    return (GRAVITY * m1 * m2) / r**2

# EARTH AND MOON OBJECTS

Earth = earth.Earth(4000)
Moon = moon.Moon(200, 300, 10, 10)

moons = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                moons.append(moon.Moon(mouse_x, mouse_y, 10, 10))
    
    screen.fill((0, 0, 0))

    Earth.draw(screen)

    Moon.draw(screen)
    r = getCenterDistance(Moon.x, Moon.y, Earth.x, Earth.y)

    if r > 0:
        F = calculateGravitation(Moon.mass, Earth.mass, r)
        ax = F * (Earth.x - Moon.x) / r / Moon.mass
        ay = F * (Earth.y - Moon.y) / r / Moon.mass
        Moon.update(ax, ay)

    for m in moons:
        m.draw(screen)
        r = getCenterDistance(m.x, m.y, Earth.x, Earth.y)
        if r > 0:
            F = calculateGravitation(m.mass, Earth.mass, r)
            ax = F * (Earth.x - m.x) / r / m.mass
            ay = F * (Earth.y - m.y) / r / m.mass
            m.update(ax, ay)


    display.update()
    clock.tick(60)

pygame.quit()