import pygame
import json
import os

# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 40
COLLECTIBLE_SIZE = 20

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Open World Game")

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Игрок
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
collected_items = []

# Функции
def save_progress():
    with open('save.json', 'w') as f:
        json.dump({'collected_items': collected_items}, f)

def load_progress():
    if os.path.exists('save.json'):
        with open('save.json', 'r') as f:
            data = json.load(f)
            return data.get('collected_items', [])
    return []

# Основной цикл игры
running = True
collected_items = load_progress()
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    # Отображение игрока
    pygame.draw.rect(screen, GREEN, (player_pos[0], player_pos[1], PLAYER_SIZE, PLAYER_SIZE))

    # Отображение собранных предметов
    for index, item in enumerate(collected_items):
        pygame.draw.rect(screen, (255, 0, 0), (item[0], item[1], COLLECTIBLE_SIZE, COLLECTIBLE_SIZE))

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Перемещение игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5
    if keys[pygame.K_UP]:
        player_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        player_pos[1] += 5

    # Проверка на столкновение с предметами
    if (player_pos[0] > SCREEN_WIDTH // 2 - 10) and (player_pos[0] < SCREEN_WIDTH // 2 + 10) and (player_pos[1] > SCREEN_HEIGHT // 2 - 10) and (player_pos[1] < SCREEN_HEIGHT // 2 + 10):
        collectible = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        if collectible not in collected_items:
            collected_items.append(collectible)
            save_progress()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()