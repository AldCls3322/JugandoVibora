from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

colors = {
    1 : 'black',
    2 : 'green',
    3 : 'blue',
    4 : 'purple',
    5 : 'yellow',
    6 : 'orange'
}

colorSnake = randrange(1, 6)
colorFood = randrange(1, 6)

while (colorFood == colorSnake):
    colorFood = randrange(1, 5)

print(colorSnake, colorFood)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    "La comida se mueve"
    if not(randint(0,100)>20):
        dx = randint(-1, 1) * 10
        dy = randint(-1, 1) * 10
        food.x += dx
        food.y += dy
        if(not inside(food)):
            food.x -= dx
            food.y -= dy
    
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, colors[colorSnake])

    square(food.x, food.y, 9, colors[colorFood])
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
