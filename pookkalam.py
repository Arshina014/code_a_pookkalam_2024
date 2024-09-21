import turtle
import math

screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)

def draw_circle(radius, color):
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_squares(radius, side, colors):
    angle = 360 / len(colors)
    for i, color in enumerate(colors):
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.setheading(i * angle)
        t.penup()
        t.forward(radius)
        t.right(75)
        t.pendown()
        t.color(color)
        t.begin_fill()
        for _ in range(7):
            t.forward(side)
            t.right(90)
        t.end_fill()

def draw_flower(x, y, petal_count, petal_size, color1, color2):
    angle = 360 / petal_count
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(petal_count):
        t.color(color1 if i % 5 == 0 else color2)
        t.begin_fill()
        t.circle(petal_size, 60)
        t.left(120)
        t.circle(petal_size, 60)
        t.left(120 - angle)
        t.end_fill()

def draw_flowers_around_circle(radius, flower_count, petal_count, petal_size, color1, color2):
    angle =400 / flower_count
    for i in range(flower_count):
        t.penup()
        t.goto(0, 0)
        t.setheading(i * angle)
        t.forward(radius)
        t.right(0)
        t.forward(petal_size)
        t.pendown()
        draw_flower(t.xcor(), t.ycor(), petal_count, petal_size, color1, color2)

def draw_triangles_around_circle(radius, side, color):
    angle = 360 / 120
    for i in range(120):
        t.penup()
        t.goto(0, 0)
        t.setheading(i * angle)
        t.forward(radius)
        t.pendown()
        t.color(color)
        t.begin_fill()
        for _ in range(3):
            t.forward(side)
            t.left(30)
        t.end_fill()

def draw_new_triangles(radius, side):
    angle = 360 / 30
    colors = ["yellow", "orange red"]
    for i in range(30):
        t.penup()
        t.goto(0, 0)
        t.setheading(i * angle)
        t.forward(radius)
        t.right(105)  # Rotate to make the triangle corner point outward
        t.pendown()
        t.color(colors[i % 2])
        t.begin_fill()
        for _ in range(3):
            t.forward(side)
            t.left(120)
        t.end_fill()

def draw_new_flowers_around_circle(radius, flower_count, petal_count, petal_size, border_color, center_color):
    angle = 360 / flower_count
    for i in range(flower_count):
        t.penup()
        t.goto(0, 0)
        t.setheading(i * angle)
        t.forward(radius)
        t.right(0)
        t.pendown()

        # Draw the flower petals
        for j in range(petal_count):
            t.color(border_color)
            t.begin_fill()
            t.circle(petal_size, 60)
            t.left(120)
            t.circle(petal_size, 60)
            t.left(120 - (360 / petal_count))
            t.end_fill()
        
        # Draw the orange circle at the center of each flower
        t.penup()
        t.goto(t.xcor(), t.ycor() - 3)  # Adjusting position for the center
        t.pendown()
        t.color(center_color)
        t.begin_fill()
        t.circle(3)  # Orange circle with radius 3
        t.end_fill()

# Drawing initial circles and patterns
draw_circle(160, "gold")
draw_circle(140, "orange red")
draw_circle(130, "orange")
draw_circle(100, "firebrick")

colors = ["yellow", "orange", "yellow", "orange", "yellow", "orange"]
draw_squares(55, 50, colors)

draw_flowers_around_circle(155, 61, 19, 10, "white", "hot pink")
draw_flowers_around_circle(140, 20, 10, 8, "crimson", "crimson")

draw_triangles_around_circle(174, 8, "green")

radii = [45, 36, 30, 20, 10]
petal_counts = [40, 30, 25, 35, 16]
colors = [("deep pink", "pink"), ("deep pink", "hot pink"), ("deep pink", "pink"), ("pink", "deep pink"), ("deep pink", "pink")]

draw_new_triangles(100, 38)

# Loop through petal counts and radii
for i in range(5):
    draw_flower(0, 0, petal_counts[i], radii[i], colors[i][0], colors[i][1])

# Drawing new layer of flowers
draw_new_flowers_around_circle(98, 72, 10, 5, "pink", "pink")

t.hideturtle()
turtle.done()
