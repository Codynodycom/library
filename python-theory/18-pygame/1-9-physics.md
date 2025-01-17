# Простая физика для 2D-игры

Сначала создадим окно игры и настроим базовые параметры для мяча, такие как его начальная позиция, радиус и цвет.

## Создание окна и настроек для мяча

<div>
    <img src="images/py-9-1.png">
</div>

1. **Создание окна**: `pygame.display.set_mode((WIDTH, HEIGHT))` — задаёт размеры окна.

2. **Рисование мяча**: `pygame.draw.circle()` рисует мяч на экране.

```python
import pygame

# Инициализация Pygame
pygame.init()

# Задаём размеры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Прыгающий мяч")
FPS = pygame.time.Clock()

# Цвета
background_color = (255, 255, 255)  # Белый фон
ball_color = (255, 0, 0)            # Красный цвет мяча

# Параметры мяча
ball_radius = 20
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_y = 0  # Начальная скорость мяча по вертикали

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():  # Обработка событий
        if event.type == pygame.QUIT:  # Проверка на закрытие окна
            running = False

    # Очистка экрана
    screen.fill(background_color)

    # Рисуем мяч
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    pygame.display.flip()  # Обновляем экран
    FPS.tick(60)

# Завершаем работу Pygame
pygame.quit()
```

## Добавление гравитации

**Гравитация** — это постоянное ускорение, направленное вниз, которое влияет на вертикальную скорость мяча. Мы добавим простую модель гравитации, которая будет увеличивать скорость мяча вниз.

<div>
    <img src="images/py-9-2.png">
</div>

1. **Гравитация**: `gravity = 0.5` — значение силы, которая будет притягивать мяч вниз.

2. **Обновление скорости**: `ball_speed_y += gravity` добавляет значение гравитации к текущей скорости мяча по вертикали, увеличивая его движение вниз.

3. **Остановка мяча**: Если мяч достигает нижней границы окна, его позиция и скорость сбрасываются.

```python
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Прыгающий мяч")
FPS = pygame.time.Clock()

background_color = (255, 255, 255)
ball_color = (255, 0, 0)

ball_radius = 20
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_y = 0
gravity = 0.5  # Сила гравитации

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Применяем гравитацию к скорости мяча по вертикали
    ball_speed_y += gravity
    ball_y += int(ball_speed_y)  # Обновляем позицию мяча с учётом скорости

    # Проверяем, чтобы мяч не упал ниже экрана
    if ball_y + ball_radius > HEIGHT:
        ball_y = HEIGHT - ball_radius
        ball_speed_y = 0  # Останавливаем мяч при касании пола

    screen.fill(background_color)
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
    pygame.display.flip()
    FPS.tick(60)

pygame.quit()
```

## Добавление прыжков

Теперь добавим возможность для мяча прыгать. Мы будем использовать пробел для активации прыжка, и ограничим высоту прыжка, чтобы мяч не поднимался слишком высоко.

<div>
    <img src="images/py-9-3.png">
</div>

1. **Прыжок**:

    - `jump_strength = -10` — значение скорости вверх, чтобы мяч "подпрыгнул".

    - При нажатии на пробел (`pygame.K_SPACE`), если мяч не в прыжке (`not is_jumping`), задаём начальную скорость прыжка и устанавливаем флаг `is_jumping = True`.

2. **Сброс прыжка**:

    - Когда мяч достигает пола, его положение и скорость сбрасываются, а флаг `is_jumping` устанавливается в `False`, позволяя игроку прыгать снова.

```python
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Прыгающий мяч")
FPS = pygame.time.Clock()

background_color = (255, 255, 255)
ball_color = (255, 0, 0)

ball_radius = 20
ball_x = WIDTH // 2
ball_y = HEIGHT - ball_radius
ball_speed_y = 0
gravity = 0.5
jump_strength = -10  # Начальная скорость прыжка (направление вверх)

running = True
is_jumping = False  # Флаг для отслеживания, находится ли мяч в прыжке

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                ball_speed_y = jump_strength  # Задаём начальную скорость для прыжка
                is_jumping = True  # Устанавливаем флаг прыжка

    # Применяем гравитацию к скорости мяча
    ball_speed_y += gravity
    ball_y += int(ball_speed_y)

    # Проверка на касание пола и сброс прыжка
    if ball_y + ball_radius >= HEIGHT:
        ball_y = HEIGHT - ball_radius
        ball_speed_y = 0
        is_jumping = False  # Сбрасываем флаг, позволяя прыгнуть снова

    screen.fill(background_color)
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
    pygame.display.flip()
    FPS.tick(60)

pygame.quit()
```

## Создание платформ для отскока

Добавим несколько платформ, от которых мяч сможет отскакивать, чтобы создать иллюзию многоуровневого прыжка.

<div>
    <img src="images/py-9-4.png">
</div>

1. **Создание платформ**:

    - `platforms` — список Rect объектов, представляющих платформы.

2. **Проверка коллизий с платформами**:

    - Если мяч касается платформы и движется вниз (`ball_speed_y > 0`), он останавливается на её поверхности, сбрасывая `ball_speed_y` и позволяя прыгнуть снова.

```python
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Прыгающий мяч")
FPS = pygame.time.Clock()

background_color = (255, 255, 255)
ball_color = (255, 0, 0)
platform_color = (0, 128, 0)

ball_radius = 20
ball_x = WIDTH // 2
ball_y = HEIGHT - ball_radius
ball_speed_y = 0
gravity = 0.5
jump_strength = -10

is_jumping = False

# Платформы
platforms = [
    pygame.Rect(150, 500, 200, 20),
    pygame.Rect(400, 420, 200, 20),
    pygame.Rect(80, 380, 200, 20)
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                ball_speed_y = jump_strength
                is_jumping = True

     # Получаем состояние всех клавиш
    keys = pygame.key.get_pressed()

    # Управление по горизонтали
    if keys[pygame.K_LEFT]:  # Если нажата клавиша "влево"
        ball_x -= 5
    if keys[pygame.K_RIGHT]:  # Если нажата клавиша "вправо"
        ball_x += 5

    # Применяем гравитацию к мячу
    ball_speed_y += gravity
    ball_y += int(ball_speed_y)

    # Проверка на касание пола
    if ball_y + ball_radius >= HEIGHT:
        ball_y = HEIGHT - ball_radius
        ball_speed_y = 0
        is_jumping = False

    # Проверка на касание платформ
    ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)
    for platform in platforms:
        if ball_rect.colliderect(platform) and ball_speed_y > 0:  # Проверка коллизии и движения вниз
            ball_y = platform.top - ball_radius  # Устанавливаем мяч на платформу
            ball_speed_y = 0
            is_jumping = False

    # Очистка экрана и рисование элементов
    screen.fill(background_color)

    # Рисуем платформы
    for platform in platforms:
        pygame.draw.rect(screen, platform_color, platform)

    # Рисуем мяч
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    pygame.display.flip()
    FPS.tick(60)

pygame.quit()
```
