import pygame
import math
import random

# Initialize pygame
pygame.init()
screen_width, screen_height = 1280, 800
screen = pygame.display.set_mode((screen_width, screen_height))

# Constants
FLY_LOOP = 50
FLY_SWERVE = 0.5
FLY_CLOCK_SPEED = 0.2  # Slower clock speed
FLY_RADIUS = 50
FLY_PULL = 0.1  # Reduced pull for less uniform synchronization
FLY_SYNC = True
MOUSE_RADIUS = 200
NUM_FIREFLIES = 150

# Utility Functions
def distance(ff1, ff2):
    return math.sqrt((ff1.x - ff2.x)**2 + (ff1.y - ff2.y)**2)

# Firefly Class
class Firefly:
    def __init__(self):
        self.x = random.random() * screen_width
        self.y = random.random() * screen_height
        self.angle = random.random() * 2 * math.pi
        self.speed = 0.5 + random.random() * 0.5
        self.swerve = (random.random() - 0.5) * FLY_SWERVE
        self.clock = random.random()

    def update(self, fireflies):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
        if self.x < -FLY_LOOP: self.x = screen_width + FLY_LOOP
        if self.x > screen_width + FLY_LOOP: self.x = -FLY_LOOP
        if self.y < -FLY_LOOP: self.y = screen_height + FLY_LOOP
        if self.y > screen_height + FLY_LOOP: self.y = -FLY_LOOP
        self.angle += self.swerve
        if random.random() < 0.05:
            self.swerve = (random.random() - 0.5) * FLY_SWERVE

        # Synchronization logic
        if FLY_SYNC:
            total_phase_diff = 0
            neighbors = 0
            for other in fireflies:
                if other is not self and distance(self, other) < FLY_RADIUS:
                    neighbors += 1
                    phase_diff = other.clock - self.clock
                    total_phase_diff += phase_diff

            if neighbors > 0:
                average_phase_diff = total_phase_diff / neighbors
                self.clock += FLY_PULL * average_phase_diff

        self.clock += FLY_CLOCK_SPEED / 60
        if self.clock > 1:
            self.clock -= 1  # Use subtraction to ensure clocks stay in sync
            for other in fireflies:  # Encourage nearby fireflies to flash soon
                if other is not self and distance(self, other) < FLY_RADIUS:
                    other.clock += FLY_PULL  # Small nudge

    def draw(self):
        # Use a sine function for sharper flash peaks
        intensity = 255 * max(0, math.sin(self.clock * math.pi * 2))
        color = (intensity, intensity, 0)
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), 5)

# Main loop
running = True
fireflies = [Firefly() for _ in range(NUM_FIREFLIES)]
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    for firefly in fireflies:
        firefly.update(fireflies)
        firefly.draw()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

# Path: Kuramato_pygame.py