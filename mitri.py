import turtle as t
t.Screen().bgcolor("darkgreen")
t.Screen().setup(500,500)
polygon = t.Turtle()
polygon.color("darkblue")
for i in range(3):
    polygon.forward(200)
    polygon.right(120)
polygon.left(60)
polygon.forward(200)
polygon.right(120)
polygon.forward(200)
t.done()