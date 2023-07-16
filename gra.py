import pygame
from pygame.locals import *

# Inicjalizacja biblioteki Pygame
pygame.init()

# Ustawienie rozmiaru okna gry
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Prosta platformówka")

# Kolory
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Stałe dotyczące postaci
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_VELOCITY = 5
JUMP_VELOCITY = 10
GRAVITY = 0.5

# Pozycja początkowa postaci
player_x = 50
player_y = HEIGHT - PLAYER_HEIGHT

# Tworzenie prostokątów-platform
platforms = [
    pygame.Rect(0, HEIGHT - 20, WIDTH, 20),
    pygame.Rect(200, HEIGHT - 100, 100, 20),
    pygame.Rect(400, HEIGHT - 200, 150, 20),
    pygame.Rect(600, HEIGHT - 300, 100, 20)
]

# Zmienne dotyczące ruchu postaci
player_velocity_y = 0
is_jumping = False

# Główna pętla gry
running = True
while running:
    # Sprawdzanie zdarzeń
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Poruszanie postaci
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and player_x > 0:
        player_x -= PLAYER_VELOCITY
    if keys[K_RIGHT] and player_x < WIDTH - PLAYER_WIDTH:
        player_x += PLAYER_VELOCITY
    if keys[K_SPACE] and not is_jumping:
        is_jumping = True
        player_velocity_y = -JUMP_VELOCITY

    # Implementacja grawitacji
    player_velocity_y += GRAVITY
    player_y += player_velocity_y

    # Sprawdzanie kolizji z platformami
    for platform in platforms:
        if player.colliderect(platform):
            # Jeżeli postać dotyka platformy, zatrzymujemy skok
            if player_velocity_y > 0:
                player_y = platform.y - PLAYER_HEIGHT
                player_velocity_y = 0
                is_jumping = False
            break

    # Rysowanie tła i postaci
    window.fill(WHITE)
    player = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)
    pygame.draw.rect(window, BLUE, player)

    # Rysowanie platform
    for platform in platforms:
        pygame.draw.rect(window, BLUE, platform)

    # Aktualizacja okna gry
    pygame.display.update()

# Zakończenie gry
pygame.quit()
