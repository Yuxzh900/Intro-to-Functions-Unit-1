import turtle
from turtle import *
t = Turtle()

t.shape('turtle')

t.speed(10)

# #Square
# for i in range(4):
#     t.forward(200)
#     t.left(90)


# #Triangle
# for i in range(3):
#     t.forward(200)
#     t.left(120)

for i in range(60):
    for i in range(4):
        t.left(90)
        t.forward(200)
    t.right(5)

turtle.done()
