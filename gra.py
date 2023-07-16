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
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Stałe dotyczące postaci
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_VELOCITY = 5
JUMP_VELOCITY = 10
GRAVITY = 0.5

# Stałe dotyczące kwadratu poruszającego się w prawo i skręcającego o 90 stopni
SQUARE_SIZE = 10
SQUARE_SPEED = 2

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

# Pozycja początkowa kwadratu poruszającego się w prawo i skręcającego o 90 stopni
square_x = player_x + PLAYER_WIDTH + SQUARE_SIZE
square_y = player_y + PLAYER_HEIGHT // 2 - SQUARE_SIZE // 2

# Kierunek ruchu kwadratu
square_direction = 1  # 1 - ruch w prawo, -1 - ruch w lewo

# Zegar dla kontroli liczby klatek na sekundę
clock = pygame.time.Clock()
FPS = 60  # Limit FPS

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
    player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)
    for platform in platforms:
        if player_rect.colliderect(platform):
            # Sprawdzanie, czy postać stoi na platformie
            if player_velocity_y > 0:
                player_y = platform.y - PLAYER_HEIGHT+2
                player_velocity_y = 0
                is_jumping = False
                break

    # Aktualizacja pozycji kwadratu poruszającego się w prawo i skręcającego o 90 stopni
    square_x += square_direction * SQUARE_SPEED

    # Sprawdzanie, czy kwadrat znajduje się wewnątrz gracza
    if square_x >= player_x + PLAYER_WIDTH:
        square_x = player_x + PLAYER_WIDTH
        square_y = player_y + PLAYER_HEIGHT // 2 - SQUARE_SIZE // 2
        square_direction = 0.25
    elif square_x + SQUARE_SIZE <= player_x:
        square_x = player_x - SQUARE_SIZE
        square_y = player_y + PLAYER_HEIGHT // 2 - SQUARE_SIZE // 2
        square_direction = -0.25

    # Rysowanie tła
    window.fill(WHITE)

    # Rysowanie ramki dla gracza
    pygame.draw.rect(window, BLACK, player_rect)

    # Rysowanie ramki dla platform
    for platform in platforms:
        pygame.draw.rect(window, BLACK, platform)

    # Rysowanie prostokątów gracza i platform
    pygame.draw.rect(window, WHITE, (player_rect.x+1, player_rect.y+1, player_rect.width-2, player_rect.height-2))
    for platform in platforms:
        pygame.draw.rect(window, WHITE, (platform.x+1, platform.y+1, platform.width-2, platform.height-2))

    # Rysowanie kwadratu poruszającego się w prawo i skręcającego o 90 stopni
    pygame.draw.rect(window, RED, (square_x, square_y, SQUARE_SIZE, SQUARE_SIZE))

    # Aktualizacja okna gry
    pygame.display.update()

    # Kontrola liczby klatek na sekundę
    clock.tick(FPS)

# Zakończenie gry
pygame.quit()
