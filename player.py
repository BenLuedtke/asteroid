import pygame

from shot import Shot

from constants import *
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
   
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self,screen):
        pygame.draw.polygon(surface=screen, color='white', points=self.triangle(),width=2)

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self,dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt*-1)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w] or keys[pygame.K_s]:
            self.move(dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

        
        self.shot_timer -= dt

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    
    def shoot(self):
        if self.shot_timer > 0:
            return
        else:
            shot = Shot(self.position.x, self.position.y,radius=SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shot_timer = PLAYER_SHOOT_COOLDOWN
