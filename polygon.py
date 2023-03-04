# Turtle script example
import turtle

t = turtle.Turtle('turtle')

angles = input("Input the amount of angles: ")

t.width(5)
angles = int(angles)
color = ['red', 'firebrick', 'yellow', 'goldenrod', 'green', 'lime', 'blue', 'dodger blue']

for i in range(angles):
    t.color(color[i % 7])
    t.forward(500 / angles)
    t.left(360 / angles)

t.penup()

turtle.done()
