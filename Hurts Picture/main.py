from turtle import Turtle ,Screen
import random

colors = [(239, 241, 240), (244, 242, 236), (229, 235, 241), (241, 224, 77), (175, 80, 32), (241, 233, 237), (214, 151, 87), (49, 36, 26), (148, 27, 41), (23, 25, 69), (45, 43, 119), (171, 21, 15), (51, 88, 156), (209, 86, 128), (127, 162, 218), (151, 54, 89), (27, 43, 28), (211, 78, 64), (139, 181, 137), (116, 110, 201)]

x = -250
y = 250
t = Turtle()
screen = Screen()
screen.colormode(255)
screen.setup(width=600, height=600)
t.penup()
t.goto(x,y)






def move_forward(colours):

    t.dot(20,random.choice(colors))
    t.forward(20)
    t.penup()
    t.forward(20)
    t.penup()
    t.forward(20)
    t.penup()

def right():
    t.penup()
    t.right(90)
    t.dot(20,random.choice(colors))
    t.forward(30)
    t.right(90)

def repeated():
    for i in range(8):
        move_forward(colors)

def left():
    t.penup()
    t.left(90)
    t.dot(10,random.choice(colors))
    t.forward(30)
    t.left(90)

for _ in range(7):
    repeated()
    right()
    repeated()
    left()


screen.mainloop()

