import turtle

t = turtle.Turtle('turtle')
angle = 30
colors = 7
ratio = 0.8
t.setheading(90)
t.pencolor((0, 1, 0))


def y(length, depth, width):
    if depth == 0:
        return
    green=min(1,max(0, (colors-depth))/colors)
    t.pencolor((0, green, 0))
    t.width(width)
    t.forward(length)
    savepos = t.pos()
    saveheading = t.heading()
    t.right(angle)
    y(length * ratio, depth - 1, max(width - 1, 1))
    t.goto(savepos)
    t.setheading(saveheading)
    t.left(angle)
    y(length * ratio, depth - 1, max(width - 1, 1))
    t.goto(savepos)
    t.setheading(saveheading)


y(length=30, depth=7, width=5)
turtle.done()
