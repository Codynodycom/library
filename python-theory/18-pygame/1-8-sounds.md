# Звуки и музыка

Pygame поддерживает различные звуковые форматы, такие как `.ogg`, `.wav` и `.mp3`. Мы будем использовать два типа звуков:

1. **Фоновая музыка**, которая будет играть на протяжении всей игры.

2. **Звуковые эффекты**, которые будут воспроизводиться при определённых действиях, таких как поворот или столкновение с препятствием.

## Подготовка звуков и музыки

Вы можете найти в интернете свои звуки или скачать по ссылкам:

- [Фоновая музыка](https://disk.yandex.kz/d/sPEBbKTfrRahnQ)
- [Звук поворота](https://disk.yandex.kz/d/KBCb-NtFdGYJsQ)
- [Звук столкновения](https://disk.yandex.kz/d/eorXWqckrzEjMg)

## Настройка окна и добавление фоновой музыки

Для начала настроим окно игры и добавим фоновую музыку, которая будет играть в бесконечном цикле.

<div>
    <img src="images/py-8-1.png">
</div>

1. **Загрузка музыки**: `pygame.mixer.music.load("background_music.mp3")` загружает фоновую музыку. Убедитесь, что у вас есть файл `background_music.mp3` в той же папке или укажите к нему путь.

2. **Запуск фоновой музыки**: `pygame.mixer.music.play(-1)` начинает воспроизведение музыки. Параметр `-1` означает, что музыка будет играть бесконечно.

```python
import pygame

# Инициализация Pygame
pygame.init()

# Задаём размеры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Звуковой лабиринт")
FPS = pygame.time.Clock()

# Загрузка фоновой музыки
pygame.mixer.music.load("background_music.mp3")  # Замените на название вашего файла
pygame.mixer.music.set_volume(0.2) # установка громкости. Максимальная громкость 1
pygame.mixer.music.play(-1)  # Цикличное воспроизведение (значение -1 указывает на бесконечный повтор)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Проверка закрытия окна
            running = False

    # Очистка экрана и обновление
    screen.fill((200, 200, 200))
    pygame.display.flip()
    FPS.tick(60)

# Завершаем работу Pygame
pygame.quit()
```

## Добавление звуковых эффектов при событиях

Теперь добавим звуковые эффекты, которые будут воспроизводиться при поворотах или столкновениях. Мы будем использовать два звука: один для поворота, другой для столкновения с препятствием.

1. **Звуковые эффекты**:

    - `turn_sound = pygame.mixer.Sound("turn_sound.wav")` загружает звуковой файл для поворотов.

    - `collision_sound = pygame.mixer.Sound("collision_sound.wav")` загружает звуковой файл для столкновений.

2. **Воспроизведение звуков при поворотах**: `turn_sound.play()` проигрывается каждый раз, когда игрок нажимает клавишу для поворота.

3. **Звук при столкновении**: Если игрок сталкивается с границами экрана, то воспроизводится `collision_sound.play()`.

```python
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Звуковой лабиринт")
FPS = pygame.time.Clock()

pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

turn_sound = pygame.mixer.Sound("turn_sound.mp3")
turn_sound.set_volume(0.1)
collision_sound = pygame.mixer.Sound("collision_sound.mp3")
collision_sound.set_volume(0.2)

player_x, player_y = WIDTH // 2, HEIGHT // 2
player_speed = 5

# Определяем стены лабиринта
walls = [
    pygame.Rect(100, 100, 600, 20),  # Верхняя горизонтальная стена
    pygame.Rect(100, 200, 20, 400),  # Левая вертикальная стена
    pygame.Rect(680, 100, 20, 400),  # Правая вертикальная стена
    pygame.Rect(100, 580, 600, 20)   # Нижняя горизонтальная стена
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Перемещение игрока с воспроизведением звука поворота
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
        turn_sound.play()
    elif keys[pygame.K_RIGHT]:
        player_x += player_speed
        turn_sound.play()
    elif keys[pygame.K_UP]:
        player_y -= player_speed
        turn_sound.play()
    elif keys[pygame.K_DOWN]:
        player_y += player_speed
        turn_sound.play()

    # Проверка столкновений с лабиринтом
    player_rect = pygame.Rect(player_x, player_y, 50, 50)
    for wall in walls:
        if player_rect.colliderect(wall):  # Проверка на столкновение с каждой стеной
            collision_sound.play()
            # Отталкиваем игрока обратно при столкновении
            if keys[pygame.K_LEFT]:
                player_x += player_speed
            elif keys[pygame.K_RIGHT]:
                player_x -= player_speed
            elif keys[pygame.K_UP]:
                player_y += player_speed
            elif keys[pygame.K_DOWN]:
                player_y -= player_speed

    # Очистка экрана и рисование элементов
    screen.fill((200, 200, 200))

    # Рисуем стены лабиринта
    for wall in walls:
        pygame.draw.rect(screen, (0, 0, 0), wall)

    # Рисуем игрока
    pygame.draw.rect(screen, (0, 128, 255), player_rect)

    pygame.display.flip()
    FPS.tick(60)

pygame.quit()
```

## Создание лабиринта и привязка звуков к взаимодействиям

Теперь добавим простой лабиринт и привяжем звуковой эффект к столкновениям с его стенами. Лабиринт можно создать с помощью прямоугольников, представляющих стены.

1. **Лабиринт**:

    - `walls` — список прямоугольников, представляющих стены лабиринта.

    - `pygame.Rect()` — создаёт объекты стен, которые затем можно использовать для проверки столкновений.

2. **Проверка столкновений с лабиринтом**:

    - Для каждого движения игрока проверяем, пересекается ли прямоугольник игрока (`player_rect`) с каждой стеной в `walls`.

    - Если столкновение обнаружено, воспроизводится `collision_sound.play()`, и игрок отталкивается обратно.

3. **Отталкивание игрока**:

    - Если игрок сталкивается со стеной при движении, его координаты корректируются, чтобы он "отскочил" обратно.

```python
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Звуковой лабиринт")
FPS = pygame.time.Clock()

pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

turn_sound = pygame.mixer.Sound("turn_sound.mp3")
turn_sound.set_volume(0.1)
collision_sound = pygame.mixer.Sound("collision_sound.mp3")
collision_sound.set_volume(0.2)

player_x, player_y = WIDTH // 2, HEIGHT // 2
player_speed = 5

# Определяем стены лабиринта
walls = [
    pygame.Rect(100, 100, 600, 20),  # Верхняя горизонтальная стена
    pygame.Rect(100, 200, 20, 400),  # Левая вертикальная стена
    pygame.Rect(680, 100, 20, 400),  # Правая вертикальная стена
    pygame.Rect(100, 580, 600, 20)   # Нижняя горизонтальная стена
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Перемещение игрока с воспроизведением звука поворота
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
        turn_sound.play()
    elif keys[pygame.K_RIGHT]:
        player_x += player_speed
        turn_sound.play()
    elif keys[pygame.K_UP]:
        player_y -= player_speed
        turn_sound.play()
    elif keys[pygame.K_DOWN]:
        player_y += player_speed
        turn_sound.play()

    # Проверка столкновений с лабиринтом
    player_rect = pygame.Rect(player_x, player_y, 50, 50)
    for wall in walls:
        if player_rect.colliderect(wall):  # Проверка на столкновение с каждой стеной
            collision_sound.play()
            # Отталкиваем игрока обратно при столкновении
            if keys[pygame.K_LEFT]:
                player_x += player_speed
            elif keys[pygame.K_RIGHT]:
                player_x -= player_speed
            elif keys[pygame.K_UP]:
                player_y += player_speed
            elif keys[pygame.K_DOWN]:
                player_y -= player_speed

    # Очистка экрана и рисование элементов
    screen.fill((200, 200, 200))

    # Рисуем стены лабиринта
    for wall in walls:
        pygame.draw.rect(screen, (0, 0, 0), wall)

    # Рисуем игрока
    pygame.draw.rect(screen, (0, 128, 255), player_rect)

    pygame.display.flip()
    FPS.tick(60)

pygame.quit()
```
