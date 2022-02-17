"""A red house on a beautiful sunny day."""

__author__ = "730425241"

from turtle import Turtle, colormode, done, tracer, update


def main() -> None:
    """The entrypoint of my scene."""
    franklin: Turtle = Turtle()
    tracer(0, 0)
    franklin.hideturtle()
    colormode(255)
    draw_square(franklin, -250, 250, 500)
    franklin.color(99, 204, 250)
    franklin.begin_fill()
    draw_rectangle(franklin, -250, 250, 500, 300)
    franklin.end_fill()
    franklin.color(59, 229, 15)
    franklin.begin_fill()
    draw_rectangle(franklin, -250, -50, 500, 200)
    franklin.end_fill()
    franklin.color("yellow")
    franklin.begin_fill()
    draw_square(franklin, -250, 250, 80)
    franklin.end_fill()
    franklin.color("red")
    franklin.begin_fill()
    draw_square(franklin, -100, 100, 200)
    franklin.end_fill()
    franklin.begin_fill()
    draw_rectangle(franklin, 40, 150, 25, 50)
    franklin.end_fill()
    franklin.color("brown")
    franklin.begin_fill()
    draw_triangle(franklin, -100, 100, 116, 200)
    franklin.end_fill()
    franklin.begin_fill()
    draw_rectangle(franklin, -20, -40, 40, 60)
    franklin.end_fill()
    draw_window(franklin, -100, 100, 50)
    draw_window(franklin, 50, 100, 50)
    update()
    done()


def draw_square(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draws a square which will be used for the overall frame of the scene, the body of the house, and the sun."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    while i < 4:
        a_turtle.forward(width)
        a_turtle.right(90)
        i += 1


def draw_rectangle(a_turtle: Turtle, x: float, y: float, width: float, length: float) -> None:
    """Draws a rectangle which will be used for the background colors, the door, and the chimney."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    while i < 2:
        a_turtle.forward(width)
        a_turtle.right(90)
        a_turtle.forward(length)
        a_turtle.right(90)
        i += 1


def draw_triangle(a_turtle: Turtle, x: float, y: float, width: float, length: float) -> None:
    """Draws a triangle which will be used for the roof of the house."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.forward(length)
    a_turtle.left(150)
    a_turtle.forward(width)
    a_turtle.left(60)
    a_turtle.forward(width)


def draw_window(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draws a square four pane window for the house in the scene."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.pencolor("black")
    a_turtle.fillcolor("white")
    a_turtle.begin_fill()
    i: int = 0
    while i < 4:
        a_turtle.forward(width)
        a_turtle.right(90)
        i += 1
    a_turtle.end_fill()
    a_turtle.forward(width / 2)
    a_turtle.right(90)
    a_turtle.forward(width)
    a_turtle.penup()
    a_turtle.goto(x, y - (width / 2))
    a_turtle.pendown()
    a_turtle.left(90)
    a_turtle.forward(width)


if __name__ == "__main__":
    main()
