from turtle import Screen, Turtle
import random

colors = []





# Create a screen
screen = Screen()
screen.colormode(255)
t = Turtle()



for i in range(1,360,5):
   r = random.randint(0,255)
   g = random.randint(0,255)
   b = random.randint(0,255)
   random_colour = (r,g,b)
   t.pencolor(random_colour)
   r = 50
   t.circle(r)
   t.right(i)
      

screen.mainloop()  # Keeps the window open
