# Обработка событий мыши

## Обработка щелчков мыши

В Pygame события, связанные с мышью, позволяют отслеживать щелчки и координаты курсора. Мы можем использовать их для взаимодействия с объектами, такими как цели в игре.

## Создание окна и обработка кликов мыши

Сначала создадим окно и настроим обработку событий кликов мыши. Когда игрок кликает по экрану, мы будем выводить координаты места щелчка, чтобы понять, где произошло взаимодействие.

<div>
    <img src="images/py-4-1.png">
</div>

1. **Обработка события нажатия мыши**: `event.type == pygame.MOUSEBUTTONDOWN` проверяет, произошло ли нажатие кнопки мыши.

2. **Координаты клика**: `event.pos` возвращает координаты места, где произошло нажатие мыши, которые сохраняются в `mouse_x` и `mouse_y`.

3. **Вывод координат**: `print()` выводит координаты клика в консоль, чтобы видеть, где именно было нажатие.

```python
import pygame

# Инициализация Pygame
pygame.init()

# Задаём размеры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Стрельба по целям")
FPS = pygame.time.Clock()

# Цвет фона
background_color = (255, 255, 255)

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():  # Обрабатываем все события
        if event.type == pygame.QUIT:  # Если событие закрытия окна
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Если произошло нажатие кнопки мыши
            mouse_x, mouse_y = event.pos  # Получаем координаты клика мыши
            print("Щелчок мыши в координатах:", mouse_x, mouse_y)

    # Заливаем экран белым цветом
    screen.fill(background_color)
    pygame.display.flip()  # Обновляем экран
    FPS.tick(60)

# Завершаем Pygame
pygame.quit()
```

## Создание движущихся целей

Теперь создадим движущиеся цели. Цели будут представлять собой круги, которые перемещаются по экрану, меняя свою позицию на каждом кадре. Игроку нужно кликать по ним, чтобы заработать очки.

<div>
    <img src="images/py-4-2.png">
</div>

1. **Создание цели**: `pygame.draw.circle()` рисует круг (цель) в заданных координатах.

2. **Перемещение цели**: `target_x += target_speed_x` и `target_y += target_speed_y` изменяют координаты цели, заставляя её двигаться.

3. **Отражение от стен**: Если цель касается границы окна, её направление меняется, чтобы создать эффект "отскока".

```python
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Стрельба по целям")
FPS = pygame.time.Clock()

background_color = (255, 255, 255)
target_color = (255, 0, 0)  # Цвет цели - красный

# Параметры цели
target_radius = 30
target_x = random.randint(target_radius, WIDTH - target_radius)
target_y = random.randint(target_radius, HEIGHT - target_radius)
target_speed_x = random.choice([-3, 3])  # Скорость по X
target_speed_y = random.choice([-3, 3])  # Скорость по Y

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление позиции цели
    target_x += target_speed_x
    target_y += target_speed_y

    # Проверка столкновения цели с границами окна
    if target_x <= target_radius or target_x >= WIDTH - target_radius:
        target_speed_x = -target_speed_x  # Меняем направление по X
    if target_y <= target_radius or target_y >= HEIGHT - target_radius:
        target_speed_y = -target_speed_y  # Меняем направление по Y

    # Рисуем фон и цель
    screen.fill(background_color)
    pygame.draw.circle(screen, target_color, (target_x, target_y), target_radius)
    pygame.display.flip()
    FPS.tick(60)

pygame.quit()
```

## Подсчёт очков за попадание

Теперь добавим функциональность для подсчёта очков. Если игрок кликает по цели, он зарабатывает одно очко, и цель перемещается в новую случайную позицию.

<div>
    <img src="images/py-4-3.png">
</div>

1. **Подсчёт очков**:

    - `score = 0` — начальное значение счёта.

    - Если игрок кликает по цели, и расстояние до центра цели меньше или равно её радиусу, то это считается попаданием.

    - `score += 1` увеличивает счёт на единицу при каждом попадании.

2. **Перемещение цели**:

    - Если игрок попадает по цели, она перемещается в новое случайное место.

3. **Отображение счёта**:

    - `font.render()` создаёт текстовое изображение для счёта, и `screen.blit(score_text, (10, 10))` отображает его в левом верхнем углу экрана.

```python
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Стрельба по целям")
FPS = pygame.time.Clock()

background_color = (255, 255, 255)
target_color = (255, 0, 0)

target_radius = 30
target_x = random.randint(target_radius, WIDTH - target_radius)
target_y = random.randint(target_radius, HEIGHT - target_radius)
target_speed_x = random.choice([-3, 3])
target_speed_y = random.choice([-3, 3])

score = 0  # Начальный счёт игрока
font = pygame.font.Font(None, 36)  # Шрифт для отображения счёта

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            # Проверка попадания по цели
            distance = ((mouse_x - target_x) ** 2 + (mouse_y - target_y) ** 2) ** 0.5
            if distance <= target_radius:
                score += 1  # Увеличиваем счёт на 1 за попадание
                print("Попадание! Текущий счёт:", score)
                # Перемещаем цель в новую случайную позицию
                target_x = random.randint(target_radius, WIDTH - target_radius)
                target_y = random.randint(target_radius, HEIGHT - target_radius)

    # Обновление позиции цели
    target_x += target_speed_x
    target_y += target_speed_y

    # Отражение от стен
    if target_x <= target_radius or target_x >= WIDTH - target_radius:
        target_speed_x = -target_speed_x
    if target_y <= target_radius or target_y >= HEIGHT - target_radius:
        target_speed_y = -target_speed_y

    # Рисуем фон, цель и счёт
    screen.fill(background_color)
    pygame.draw.circle(screen, target_color, (target_x, target_y), target_radius)
    
    # Отображение счёта на экране
    score_text = font.render("Счёт: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    FPS.tick(60)

pygame.quit()
```
