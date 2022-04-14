from turtle import Turtle, Screen
import turtle
import random
color_list = [ (207, 166, 126),  (139, 48, 106), (164, 169, 38), (244, 79, 56), (3, 143, 57), (214, 233, 231), (241, 66, 140), (1, 143, 184), (241, 102, 162), (162, 55, 51), (49, 203, 226), (254, 230, 0), (21, 166, 126), (209, 234, 237), (243, 223, 51), (165, 182, 172), (27, 196, 219), (233, 165, 191), (141, 213, 225), (243, 170, 152), (159, 210, 180), (107, 45, 102), (191, 191, 193), (10, 116, 37), (150, 41, 37)]

turtle.colormode(255)
tim = Turtle()
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(100)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)







wn = Screen()
wn.exitonclick()

