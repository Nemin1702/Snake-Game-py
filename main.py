import turtle
import random
import time
window=turtle.Screen()
window.title('Snake Game')
window.setup(width=700,height=700)
window.tracer(0)
turtle.bgcolor('black')

turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color('red')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

snake=turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color('blue')
snake.penup()
snake.goto(0,0)
snake.direction="stop"

fruit=turtle.Turtle()
fruit.speed(0)
fruit.shape('circle')
fruit.color('green')
fruit.penup()
fruit.goto(50,0)

score=turtle.Turtle()
score.speed(0)
score.color('white')
score.penup()
score.goto(0,300)
score.write('Score: ',align="center", font=('courier', 24, "bold"))
score.hideturtle()

def snake_go_up():
    if snake.direction != "down":
        snake.direction="up"
def snake_go_down():
    if snake.direction != "up":
        snake.direction="down"
def snake_go_left():
    if snake.direction !="right":
        snake.direction="left"
def snake_go_right():
    if snake.direction !="left":
        snake.direction="right"

def snake_move():
    if snake.direction=="up":
        y=snake.ycor()
        snake.sety(y+20)
    if snake.direction=="down":
        y=snake.ycor()
        snake.sety(y-20)
    if snake.direction=="left":
        x=snake.xcor()
        snake.setx(x-20)
    if snake.direction=="right":
        x=snake.xcor()
        snake.setx(x+20)

window.listen()
window.onkeypress(snake_go_up,'Up')
window.onkeypress(snake_go_down,'Down')
window.onkeypress(snake_go_left,'Left')
window.onkeypress(snake_go_right,'Right')

points=0
delay=0.2
old_fruit=[]
while True:
    window.update()
    if snake.distance(fruit)< 20:
        x=random.randint(-290,270)
        y=random.randint(-240,240)
        fruit.goto(x,y)
        score.clear()
        points+=1
        score.write('score:{}'.format(points),align="center", font=('courier', 24, "bold"))
        delay-=0.01
        new_fruit=turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape('square')
        new_fruit.color('blue')
        new_fruit.penup()
        old_fruit.append(new_fruit)
    for index in range(len(old_fruit)-1,0,-1):
        a=old_fruit[index-1].xcor()
        b=old_fruit[index-1].ycor()
        old_fruit[index].goto(a,b)
    if len(old_fruit)>0:
        a=snake.xcor()
        b=snake.ycor()
        old_fruit[0].goto(a,b)
    snake_move()
    if snake.xcor()>280 or snake.xcor()<-300 or snake.ycor()>240 or snake.ycor()<-240:
        time.sleep(1)
        window.clear()
        window.bgcolor('red')
        score.goto(0,0)
        score.write("Game Over\nYour score is {}".format(points),align="center", font=('courier', 24, "bold"))
    for food in old_fruit:
        if food.distance(snake)<20:
            time.sleep(1)
            window.clear()
            window.bgcolor('red')
            score.goto(0,0)
            score.write("Game Over\nYour score is {}".format(points),align="center", font=('courier', 24, "bold"))
    time.sleep(delay)


turtle.Terminator()