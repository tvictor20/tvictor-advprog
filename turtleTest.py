import turtle

window = turtle.Screen()
t = turtle.Turtle()

t.speed(10)
window.bgcolor("green")
for i in range(4):
    t.color("red")
    t.forward(100)
    t.left(90)

t2 = turtle.Turtle()

t2.speed(0)

for i in range(360):
    t2.forward(1)
    t2.left(1)


window.exitonclick()
