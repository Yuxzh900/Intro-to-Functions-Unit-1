import turtle
from turtle import *
t = Turtle()

t.shape('turtle')

# t.forward(200)

# def square (x):
#     t.forward(x)
#     t.left(90)
#     t.forward(x)
#     t.left(90)
#     t.forward(x)
#     t.left(90)
#     t.forward(x)
#     t.left(90)
# square(200)

# def triangle (y):
#     t.forward(y)
#     t.left(120)
#     t.forward(y)
#     t.left(120)
#     t.forward(y)
#     t.left(120)
# triangle(200)

def Righttriangle():
    t.left(90)
    t.forward(142)
    t.left(135)
    t.forward(200)
    t.left(135)
    t.forward(142)
Righttriangle()

def message(input):
    print(input)
message("The turtle and the rabbit")

turtle.done()