import turtle

# Создание экрана
screen = turtle.Screen()
screen.title("Пять черепах")
screen.bgcolor("cyan")

# Первая черепаха — круг
t1 = turtle.Turtle()
t1.shape("turtle")
t1.color("blue")
t1.pensize(3)
t1.penup()
t1.goto(-200, 170)
t1.pendown()

# Рисует круг
t1.circle(50)

# Вторая черепаха — знак олимпиады
t2 = turtle.Turtle()
t2.shape("turtle")
t2.color("black")
t2.pensize(2)
t2.penup()
t2.goto(-50, 150)
t2.pendown()

# Рисует олимпийские кольца
olympic_colors = ["blue", "black", "red", "yellow", "green"]
positions = [(-100, 0), (0, 0), (100, 0), (-50, -50), (50, -50)]
t2.speed(0)

for i in range(5):
    t2.penup()
    t2.goto(positions[i])
    t2.color(olympic_colors[i])
    t2.pendown()
    t2.circle(50)

# Третья черепаха — пентаграмма
t3 = turtle.Turtle()
t3.shape("triangle")
t3.color("purple")
t3.pensize(3)
t3.penup()
t3.goto(-250, -150)
t3.pendown()

# Рисует пентаграмму
for _ in range(5):
    t3.forward(200)
    t3.right(144)

# Четвёртая черепаха — цветной дом
t4 = turtle.Turtle()
t4.shape("square")
t4.color("brown")
t4.pensize(4)
t4.penup()
t4.goto(200, 200)
t4.pendown()

# Рисует квадрат (стены дома)
t4.fillcolor("orange")
t4.begin_fill()
for _ in range(4):
    t4.forward(100)
    t4.right(90)
t4.end_fill()

# Рисует треугольник (крыша)
t4.fillcolor("red")
t4.begin_fill()
t4.goto(250, 300)  # Верхний угол крыши
t4.goto(300, 200)  # Правая точка крыши
t4.goto(200, 200)  # Левая точка крыши
t4.end_fill()

# Пятая черепаха — спиральный узор
t5 = turtle.Turtle()
t5.shape("circle")
t5.color("green")
t5.pensize(2)
t5.penup()
t5.goto(200, -200)
t5.pendown()

# Рисует спираль
length = 10
for _ in range(50):
    t5.forward(length)
    t5.right(105)
    length += 2

# Завершение программы
screen.mainloop()
