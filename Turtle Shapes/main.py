from turtle import Screen, Turtle

# Create a screen
screen = Screen()
t = Turtle()

turns =list(range(4,11))

for i in range(len(turns)):
    number_of_turns = turns[i]
    for i in range(number_of_turns):
        angle=360/number_of_turns
        t.forward(50)
        t.right(angle)
print(number_of_turns)


screen.mainloop()  # Keeps the window open
