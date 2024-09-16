import turtle as t
t.Screen().bgcolor("darkgreen")
t.Screen().setup(500,500)
polygon = t.Turtle()
polygon.color("darkblue")
size = 0
while True:
    for i in range(4):
        polygon.forward(size+1)
        polygon.left(90)
        size = size -2
    size = size + 1
t.done()