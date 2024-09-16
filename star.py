import turtle as t
t.Screen().bgcolor("darkgreen")
t.Screen().setup(500,500)
polygon = t.Turtle()
for i in range(3):
    polygon.forward(200)
    polygon.right(120)
polygon.right(90)
polygon.penup()
polygon.forward(100)
polygon.pendown()
polygon.left(90)
for i in range(3):
    polygon.forward(200)
    polygon.left(120)
t.done()