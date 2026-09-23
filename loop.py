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

# def squares(x):
#     for i in range(60):
#         for i in range(4):
#             t.forward(x)       
#             t.left(90)
#         t.right(5)
# squares(200)

# sidelength = 100
# rotate = 90
# def square(x,y):
#     for i in range(4):
#         t.forward(x)
#         t.left(y)
# square(0,90)

# def doublingsquares(irange):
#     length = (25)
#     for i in range(irange):
#         square(length, 90)
#         length = length * 2
# doublingsquares(5)

# def addingsqaures(irange):
#     length = 25
#     for i in range(irange):
#         square (length, 90)
#         length += 25
# addingsqaures(5)

# def sqaurespiral(irange):
#     length = 5
#     for i in range(irange):
#         square (length, 90) 
#         length += 5
#         t.right(5)
# sqaurespiral(60)

sidelength = 100
rotate = 144
def star(x,y):
    for i in range(5):
        t.left(y)
        t.forward(x)
star(0,144)

def sprialstar(irange):
    length = 5
    for i in range(irange):
        star (length,144)
        length += 5
        t.right(5)
sprialstar(100)

turtle.done()
