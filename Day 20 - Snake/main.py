from turtle import Screen, Turtle
x_positions = [0, -20, -40]

for snake_square in range(0, 3):
    snake_segment = Turtle("square")
    snake_segment.color("white")
    snake_segment.setx(x_positions[snake_square])












screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")



screen.exitonclick()