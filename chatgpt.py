import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (135, 206, 250)
GREEN = (0, 200, 0)
RED = (255, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Game variables
bird_x = 50
bird_y = HEIGHT // 2
bird_radius = 20
bird_vel = 0
gravity = 0.5
jump_strength = -10

pipe_width = 70
pipe_gap = 150
pipe_velocity = 3
pipes = []

score = 0
font = pygame.font.SysFont(None, 40)

# Function to create new pipes
def create_pipe():
    height = random.randint(100, HEIGHT - 200)
    top = pygame.Rect(WIDTH, 0, pipe_width, height)
    bottom = pygame.Rect(WIDTH, height + pipe_gap, pipe_width, HEIGHT - (height + pipe_gap))
    return top, bottom

# Add initial pipes
for i in range(2):
    pipes.extend(create_pipe())
    pipes[-2].x += i * 300
    pipes[-1].x += i * 300

# Main game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLUE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_vel = jump_strength

    # Bird movement
    bird_vel += gravity
    bird_y += bird_vel
    pygame.draw.circle(screen, RED, (bird_x, int(bird_y)), bird_radius)

    # Pipes movement
    for pipe in pipes:
        pipe.x -= pipe_velocity
        pygame.draw.rect(screen, GREEN, pipe)

    # Recycle pipes
    if pipes[0].x + pipe_width < 0:
        pipes.pop(0)
        pipes.pop(0)
        pipes.extend(create_pipe())

    # Collision detection
    bird_rect = pygame.Rect(bird_x - bird_radius, bird_y - bird_radius, bird_radius*2, bird_radius*2)
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            running = False

    if bird_y - bird_radius < 0 or bird_y + bird_radius > HEIGHT:
        running = False

    # Scoring
    for pipe in pipes[::2]:
        if pipe.x + pipe_width == bird_x:
            score += 1

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.update()

# Game Over
pygame.quit()   











