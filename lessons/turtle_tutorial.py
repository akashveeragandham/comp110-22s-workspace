from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.penup()
leo.goto(-150, -100)
leo.pendown()
leo.color("blue")
colormode(255)
leo.color(99, 204, 250)
leo.pencolor("pink")
leo.fillcolor(32, 67, 93)
leo.color("green", "yellow")
leo.speed(50)
leo.hideturtle()

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()

done()