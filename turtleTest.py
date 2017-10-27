import turtle

window = turtle.Screen()
window.bgpic("earth.gif")
window.bgcolor("black")
t = turtle.Turtle()
t.color("red")
t.shape("turtle")
t.fillcolor("purple")
t.speed(5)
t.circle(100,180)
t.begin_poly()
t.fillcolor("white")
t.fill(True)
for i in range(4):
    t.forward(100)
    t.left(90)

t.end_poly()
t.fill(False)

t2 = turtle.Turtle()
t2.color("yellow")
t2.speed(5)
t2.shape("classic")
t2.fillcolor("orange")
t2.fill(True)
t2.circle(50, 360)
t2.fill(False)


window.exitonclick()
