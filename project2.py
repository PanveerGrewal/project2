import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("skyblue")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(0)

# Draw the ground
pen.penup()
pen.goto(-300, -200)
pen.pendown()
pen.color("limegreen")
pen.begin_fill()
pen.goto(300, -200)
pen.goto(300, -100)
pen.goto(-300, -100)
pen.goto(-300, -200)
pen.end_fill()

# Draw the sun
pen.penup()
pen.goto(-250, 150)
pen.pendown()
pen.color("yellow")
pen.begin_fill()
pen.circle(50)
pen.end_fill()

# Function to draw a rectangle
def draw_rectangle(x, y, width, height, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("black", color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.end_fill()

# Function to draw a triangle
def draw_triangle(x, y, base, height, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("black", color)
    pen.begin_fill()
    pen.goto(x + base / 2, y + height)
    pen.goto(x + base, y)
    pen.goto(x, y)
    pen.end_fill()

# Draw the hut
base_width = 200
base_height = 100
roof_width = 250
roof_height = 150

# Draw the base of the hut
draw_rectangle(50, -100, base_width, base_height, "orange")

# Draw the roof of the hut
draw_triangle(25, 0, roof_width, roof_height, "red")

# Draw the door
door_width = 40
door_height = 80
draw_rectangle(95, -100, door_width, door_height, "brown")

# Function to draw a flower
def draw_flower(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("brown")
    pen.goto(x, y + 15)
    pen.color("green")
    pen.begin_fill()
    pen.goto(x - 10, y + 30)
    pen.goto(x, y + 45)
    pen.goto(x + 10, y + 30)
    pen.goto(x, y + 15)
    pen.end_fill()

# Draw flowers
draw_flower(-50, -100)
draw_flower(50, -100)
draw_flower(-150, -100)
draw_flower(150, -100)

# Hide the turtle
pen.hideturtle()

# Exit on click
turtle.done()
