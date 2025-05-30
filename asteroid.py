import pygame
import random

from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self,screen):
        pygame.draw.circle(surface=screen, color='white', center=(self.position),radius=self.radius,width=2)

    def update(self,dt):
        self.position += self.velocity*dt

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        new_angle_1 = self.velocity.rotate(angle)
        new_angle_2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, radius=new_radius)
        new_asteroid_1.velocity = new_angle_1*1.2
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, radius=new_radius)
        new_asteroid_2.velocity = new_angle_2*1.2
        