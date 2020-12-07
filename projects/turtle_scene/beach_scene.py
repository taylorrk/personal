"""The beach at night time.""" """The parameter.circle() function was used to create the moon and the sand."""

__author__ = "730322626"

from turtle import Turtle, colormode, done, tracer, update


FASTEST_SPEED: int = 0


def main() -> None:
    """The entry point of my scene."""
    tracer(0, 0)
    ocean_water = Turtle()
    star = Turtle()
    moon = Turtle()
    sand = Turtle()
    sky = Turtle()
    draw_sky(sky, -360, -360)
    draw_ocean_water(ocean_water, -360.0, -90.0)
    draw_stars(star, 150, 100)
    draw_stars(star, 300, 250)
    draw_stars(star, 0, 250)
    draw_moon(moon, -250, 150)
    draw_sand(sand, -360, -360)
    update()
    done()


def draw_sky(sky: Turtle, x: float, y: float) -> None:
    """This function makes the screen black to represent the night sky."""
    colormode(255)
    sky.penup()
    sky.goto(x, y)
    sky.pendown()
    sky.color(0, 0, 0)
    sky.speed(FASTEST_SPEED)
    sky.begin_fill()
    i: int = 0
    while (i < 4):
        sky.forward(800)
        sky.left(90)
        i = i + 1
    sky.end_fill()
    return


def draw_ocean_water(ocean_water: Turtle, x: float, y: float) -> None:
    """This function draws the ocean water."""
    colormode(255)
    ocean_water.penup()
    ocean_water.goto(x, y)
    ocean_water.setheading(0.0)
    ocean_water.pendown()
    ocean_water.color(0, 191, 255)
    ocean_water.speed(FASTEST_SPEED)
    ocean_water.begin_fill()
    i: int = 0
    while (i < 9):
        ocean_water.forward(41)
        ocean_water.left(20)
        ocean_water.forward(41)
        ocean_water.right(22.25)
        i = i + 1
    ocean_water.left(110)
    ocean_water.backward(260)
    ocean_water.left(90)
    ocean_water.forward(800)
    ocean_water.end_fill()
    return 


def draw_stars(star: Turtle, x: float, y: float) -> None:
    """This function draws the stars in the night sky."""
    colormode(255)
    star.penup()
    star.goto(x, y)
    star.pendown()
    star.color(255, 215, 0)
    star.speed(FASTEST_SPEED)
    i: int = 0
    while (i < 5):
        star.right(144)
        star.forward(100)
        i = i + 1
    return


def draw_moon(moon: Turtle, x: float, y: float) -> None:
    """This function draws the moon in the night sky."""
    radius: int = 75
    colormode(255)
    moon.penup()
    moon.goto(x, y)
    moon.pendown()
    moon.color(220, 220, 220)
    moon.speed(FASTEST_SPEED)
    moon.begin_fill()
    moon.circle(radius)
    moon.end_fill()
    return


def draw_sand(sand: Turtle, x: float, y: float) -> None:
    """This function draws the sand on the beach."""
    radius: int = 80
    shift_x_coordinate_right: int = 80
    colormode(255)
    i: int = 0
    while i < 10:
        sand.penup()
        sand.goto(x, y)
        sand.pendown()
        sand.color(222, 184, 135)
        sand.begin_fill()
        sand.speed(FASTEST_SPEED)
        sand.circle(radius)
        sand.end_fill()
        x = x + (shift_x_coordinate_right)
        i = i + 1
    return


if __name__ == "__main__":
    main()
else:
    print(__name__)