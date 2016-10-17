import turtle

def draw_on_window():
    window = turtle.Screen()
    window.bgcolor("black")
    # Create a turtle Brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("yellow")
    brad.speed(10)
    for i in range(1, 36):
        draw_square(brad)
        brad.right(10)
    # Create a turtle Angie - Draws a Circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    draw_circle(angie)
    # Creates a turtle Minsoo - Draws a Triangle
    minsoo = turtle.Turtle()
    minsoo.shape("triangle")
    minsoo.color("purple")
    draw_triangle(minsoo)
    # Create a turtle Anastasia - Draws a Tree
    anastasia = turtle.Turtle()
    anastasia.shape("turtle")
    anastasia.color("magenta")
    anastasia.speed(10)
    anastasia.lt(90)
    anastasia.up()
    anastasia.bk(100)
    anastasia.down()
    draw_tree(anastasia, 100)
    # Creates a turtle Daisy - Draws a Fractal
    daisy = turtle.Turtle()
    daisy.shape("turtle")
    daisy.color("green")
    daisy.speed(10)
    draw_fractals(daisy, 500, 4)
    window.exitonclick()

def draw_tree(some_turtle, length):
    if length > 0:
        some_turtle.forward(length)
        some_turtle.lt(30)
        draw_tree(some_turtle, length-10)
        some_turtle.rt(60)
        draw_tree(some_turtle, length-10)
        some_turtle.lt(30)
        some_turtle.bk(length)

def draw_square(some_turtle):
    for i in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_circle(some_turtle):
    some_turtle.circle(100)

def draw_triangle(some_turtle):
    for i in range(3):
        some_turtle.back(100)
        some_turtle.right(120)

def draw_fractals(some_turtle, length, depth):
    if depth == 0:
        draw_fractals.forward(length)
    else:
        draw_fractals(some_turtle, length/3, depth-1)
        some_turtle.rt(60)
        draw_fractals(some_turtle, length/3, depth-1)
        some_turtle.lt(120)
        draw_fractals(some_turtle, length/3, depth-1)
        some_turtle.rt(60)
        draw_fractals(some_turtle, length/3, depth-1)

draw_on_window()
