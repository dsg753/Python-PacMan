import pygame
import sys
import random
from pygame.locals import *

# Constants
WIDTH, HEIGHT = 640, 480
PACMAN_SIZE = 20
PELLET_SIZE = 5
GHOST_SIZE = 20
PACMAN_SPEED = 5
GHOST_SPEED = 3
FPS = 30

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()
pygame.mixer.init()  # Initialize the mixer module for sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pac-Man')

# Load sounds
eat_sound = pygame.mixer.Sound('pacman_chomp.wav')
death_sound = pygame.mixer.Sound('pacman_death.wav')  # Load the death sound

# Walls layout
walls = [
    pygame.Rect(50, 50, 540, 20),
    pygame.Rect(50, 50, 20, 380),
    pygame.Rect(570, 50, 20, 380),
    pygame.Rect(50, 410, 540, 20),
   
]

# Pellet coordinates
pellets = [(x, y) for x in range(60, WIDTH - 60, 50) for y in range(60, HEIGHT - 60, 50)]

# Ghosts
ghosts = [{'x': random.randint(GHOST_SIZE, WIDTH - GHOST_SIZE), 
           'y': random.randint(GHOST_SIZE, HEIGHT - GHOST_SIZE), 
           'direction': random.choice(['LEFT', 'RIGHT', 'UP', 'DOWN'])} 
          for _ in range(3)]

# Game clock
clock = pygame.time.Clock()

def draw_pacman(x, y):
    pygame.draw.circle(screen, YELLOW, (x, y), PACMAN_SIZE)

def draw_pellets(pellets):
    for pellet in pellets:
        pygame.draw.circle(screen, WHITE, pellet, PELLET_SIZE)

def draw_ghosts(ghosts):
    for ghost in ghosts:
        pygame.draw.circle(screen, RED, (ghost['x'], ghost['y']), GHOST_SIZE)

def draw_walls(walls):
    for wall in walls:
        pygame.draw.rect(screen, BLUE, wall)

def move_pacman(x, y, direction, walls):
    original_x, original_y = x, y
    
    if direction == 'LEFT':
        x -= PACMAN_SPEED
    elif direction == 'RIGHT':
        x += PACMAN_SPEED
    elif direction == 'UP':
        y -= PACMAN_SPEED
    elif direction == 'DOWN':
        y += PACMAN_SPEED
    
    x = max(PACMAN_SIZE, min(WIDTH - PACMAN_SIZE, x))
    y = max(PACMAN_SIZE, min(HEIGHT - PACMAN_SIZE, y))
    
    pacman_rect = pygame.Rect(x - PACMAN_SIZE, y - PACMAN_SIZE, PACMAN_SIZE * 2, PACMAN_SIZE * 2)
    
    for wall in walls:
        if pacman_rect.colliderect(wall):
            return original_x, original_y  # Return to original position if there's a collision

    return x, y

def move_ghosts(ghosts, walls):
    for ghost in ghosts:
        original_x, original_y = ghost['x'], ghost['y']
        
        if ghost['direction'] == 'LEFT':
            ghost['x'] -= GHOST_SPEED
        elif ghost['direction'] == 'RIGHT':
            ghost['x'] += GHOST_SPEED
        elif ghost['direction'] == 'UP':
            ghost['y'] -= GHOST_SPEED
        elif ghost['direction'] == 'DOWN':
            ghost['y'] += GHOST_SPEED

        if ghost['x'] <= GHOST_SIZE or ghost['x'] >= WIDTH - GHOST_SIZE:
            ghost['direction'] = 'RIGHT' if ghost['direction'] == 'LEFT' else 'LEFT'
        if ghost['y'] <= GHOST_SIZE or ghost['y'] >= HEIGHT - GHOST_SIZE:
            ghost['direction'] = 'DOWN' if ghost['direction'] == 'UP' else 'UP'
        
        ghost_rect = pygame.Rect(ghost['x'] - GHOST_SIZE, ghost['y'] - GHOST_SIZE, GHOST_SIZE * 2, GHOST_SIZE * 2)
        
        for wall in walls:
            if ghost_rect.colliderect(wall):
                ghost['x'], ghost['y'] = original_x, original_y
                ghost['direction'] = random.choice(['LEFT', 'RIGHT', 'UP', 'DOWN'])

def check_pacman_ghost_collision(pacman_x, pacman_y, ghosts):
    pacman_rect = pygame.Rect(pacman_x - PACMAN_SIZE, pacman_y - PACMAN_SIZE, PACMAN_SIZE * 2, PACMAN_SIZE * 2)
    for ghost in ghosts:
        ghost_rect = pygame.Rect(ghost['x'] - GHOST_SIZE, ghost['y'] - GHOST_SIZE, GHOST_SIZE * 2, GHOST_SIZE * 2)
        if pacman_rect.colliderect(ghost_rect):
            print("Collision detected!")  # Debugging statement
            death_sound.play()  # Play death sound on collision with a ghost
            return True
    return False

def check_collisions(x, y, pellets):
    pacman_rect = pygame.Rect(x - PACMAN_SIZE, y - PACMAN_SIZE, PACMAN_SIZE * 2, PACMAN_SIZE * 2)
    new_pellets = []
    for pellet in pellets:
        if not pacman_rect.collidepoint(pellet):
            new_pellets.append(pellet)
        else:
            eat_sound.play()  # Play the sound when Pac-Man eats a pellet
    return new_pellets

def main():
    pacman_x, pacman_y = 100, 150  # Updated Pac-Man's starting position
    direction = 'RIGHT'
    
    global pellets
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    direction = 'LEFT'
                elif event.key == K_RIGHT:
                    direction = 'RIGHT'
                elif event.key == K_UP:
                    direction = 'UP'
                elif event.key == K_DOWN:
                    direction = 'DOWN'

        pacman_x, pacman_y = move_pacman(pacman_x, pacman_y, direction, walls)
        move_ghosts(ghosts, walls)
        
        if check_pacman_ghost_collision(pacman_x, pacman_y, ghosts):
            print("Game Over!")
            pygame.quit()
            sys.exit()

        pellets = check_collisions(pacman_x, pacman_y, pellets)
        if not pellets:
            print("You Win!")
            pygame.quit()
            sys.exit()

        screen.fill(BLACK)
        draw_pacman(pacman_x, pacman_y)
        draw_pellets(pellets)
        draw_walls(walls)
        draw_ghosts(ghosts)
        pygame.display.flip()

        clock.tick(FPS)

if __name__ == '__main__':
    main()
