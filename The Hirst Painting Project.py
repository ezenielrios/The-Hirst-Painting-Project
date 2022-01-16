import turtle as turtle_module
import random

#Adjust to 255 for RGB values
turtle_module.colormode(255)

squirt = turtle_module.Turtle()
squirt.speed("fastest")
squirt.penup()
squirt.hideturtle()

#RGB Values from turtle module for dots
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

#set starting point and direction
squirt.setheading(225)
squirt.forward(300)
squirt.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    squirt.dot(20, random.choice(color_list))
    squirt.forward(50)

    if dot_count % 10 == 0:
        squirt.setheading(90)
        squirt.forward(50)
        squirt.setheading(180)
        squirt.forward(500)
        squirt.setheading(0)

#Screen Object to keep painting on screen until click
screen = turtle_module.Screen()
screen.exitonclick()